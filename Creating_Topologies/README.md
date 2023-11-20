# Creating Topologies 
## Các classes, methods, functions và variables trong đoạn mã: 
- `Topo`: lớp cơ sở cho cấu trúc liên kết Mininet
- `build()`: phương thức ghi đè trong lớp cấu trúc liên kết (topology class)
- `addSwitch()`: thêm một switch vào Topo và trả về tên switch
- `addHost()`: thêm máy chủ vào Topo -> returns the host name
- `addLink()`: thêm liên kết hai chiều vào Topo (các liên kết trong Mininet là hai chiều trừ khi có ghi chú khác)
- `Mininet`: lớp chính để tạo và quản lý mạng
- `start()`: khởi động mạng của bạn
- `pingAll()`: kiểm tra kết nối bằng cách cố gắng để tất cả các nút ping lẫn nhau
- `stop()`: stops your network
- `net.hosts`: tất cả các máy chủ trong mạng
- `dumpNodeConnections()`: kết nối các kết nối từ một tập hợp các nút.
- `setLogLevel( 'info' | 'debug' | 'output' )`: đặt mức đầu ra mặc định của Mininet ('info' is recommended)
## Note:  Mininet() and constructor functions 
- Phân biệt giữa constructors (hàm trả về đối tượng) và objects (đối tượng :Đ)
- Mininet() là hàm tạo tạo và trả về đối tượng mạng Mininet. Nó cần một số tham số cấu hình, đáng chú ý là:
  + `topo`: một đối tượng cấu trúc liên kết
  + `host`: hàm tạo được sử dụng để tạo Host elements trong cấu trúc liên kết
  + `switch`: một hàm tạo được sử dụng để tạo các phần tử Switch trong cấu trúc liên kết
  + `controller`: một hàm tạo được sử dụng để tạo các phần tử Bộ điều khiển trong cấu trúc liên kết
  + `link`: một hàm tạo được sử dụng để tạo Liên kết trong cấu trúc liên kết
  + Note: vì `host`, `switch`, `controller` và `link` là các hàm tạo nên chúng không được gọi trực tiếp.
