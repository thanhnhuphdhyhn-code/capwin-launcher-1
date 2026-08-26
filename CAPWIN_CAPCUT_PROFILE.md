# Preset CapCut — Redmi Turbo 3

## Giá trị khi tạo container mới

| Thuộc tính | Giá trị khởi đầu | Lý do |
|---|---|---|
| Tên container | `CapCut — Redmi Turbo 3` | Giúp phân biệt profile thử CapCut với container khác. |
| Màn hình | 1280×720 | Giá trị container mặc định của fork, phù hợp bắt đầu smoke test UI. |
| Graphics driver | Driver mặc định theo thiết bị | Fork tự chọn theo GPU; trên Adreno cần xác minh Turnip trên máy thật. |
| DirectX wrapper | DXVK | Giá trị mặc định của container, có thể chuyển WineD3D khi log cho thấy lỗi renderer. |
| Box64 | Performance | Ưu tiên tốc độ theo profile, nhưng có thể chuyển Stability nếu CapCut crash/đứng. |
| Startup | Essential | Giá trị fork mặc định, giảm dịch vụ Windows không cần thiết lúc thử. |

## Cách dùng an toàn

Preset này chỉ được áp dụng khi **tạo container mới**. Sau đó vẫn phải chọn Wine/runtime hợp lệ, nhập `CapCut.exe` hoặc installer do người dùng tự tải, và kiểm tra log Wine/Box64. Nếu CapCut dừng ở splash screen, thử preset Stability trước khi thay đổi nhiều biến môi trường. Nếu cửa sổ có nhưng video preview lỗi, kiểm tra renderer/driver bằng ứng dụng Windows nhẹ trước.

> Không có preset nào biến CapCut Windows thành ứng dụng Android native. Tương thích cuối cùng phụ thuộc cụ thể vào bản CapCut, Wine/Box64, driver Vulkan, codec và Android trên thiết bị.
