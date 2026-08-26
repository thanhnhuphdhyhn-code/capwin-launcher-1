# CapWin Launcher — Upstream attribution and licensing checklist

CapWin Launcher là fork được tùy biến từ Winlator. Cần giữ nguyên toàn bộ bản quyền, license và thông báo upstream trong source và trong bản phân phối.

| Thành phần | Vai trò | Nguồn/giấy phép cần kiểm tra trước phân phối |
|---|---|---|
| Winlator | Container, Android UI, phần native | Upstream `brunodev85/winlator`, root LICENSE LGPL-2.1 |
| Wine | Lớp tương thích Windows | WineHQ source và license tại commit đang dùng |
| Box86 / Box64 | Dịch mã x86/x86_64 | `ptitSeb` source và license theo commit runtime |
| Mesa (Turnip/Zink/VirGL) | Driver/renderer | Mesa source và license từng thành phần |
| DXVK | Direct3D sang Vulkan | `doitsujin/dxvk`, Zlib license |
| VKD3D, CNC DDraw, wine addons | Thành phần runtime bổ sung | License theo source/binary commit được pin |
| Gladio, Vortek, Android ALSA, libadrenotools | Thành phần native/submodule | License file trong từng source tree |

## Điều kiện phân phối

Không đưa CapCut hoặc nội dung sở hữu độc quyền vào repository hay APK. Với mọi binary runtime được đóng gói, lưu phiên bản, URL source, checksum, license, notice và phương thức người dùng truy cập source tương ứng. Các thay đổi source của fork phải có ghi chú thay đổi theo yêu cầu license áp dụng.

> Tài liệu này là checklist kỹ thuật, không thay thế tư vấn pháp lý. Cần kiểm tra license tại chính commit/binary được phân phối trước khi phát hành công khai.
