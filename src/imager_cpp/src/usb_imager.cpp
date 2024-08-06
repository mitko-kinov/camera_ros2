#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>


class ImagerNode : public rclcpp::Node
{
public:
    ImagerNode() : Node("imager_node")
    {
        subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
            "usbcam_image",
            10,
            std::bind(&ImagerNode::callback_imager, this, std::placeholders::_1)
        );
    }
private:
    void callback_imager(const sensor_msgs::msg::Image::SharedPtr msg) const
    {
        cv_bridge::CvImagePtr cv_ptr;
        try
        {
            cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
        }
        catch(cv_bridge::Exception& e)
        {
            RCLCPP_ERROR(this->get_logger(), "cv_bridge execption: %s", e.what());
            return;
        }

        cv::imshow("USB Camera", cv_ptr->image);
        cv::waitKey(1);
    }

    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
};


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ImagerNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}