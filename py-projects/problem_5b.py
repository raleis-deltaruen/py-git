formats = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
def print_format(file: str) -> str:
    result = file
    file_nameparts = result.split(".")
    if len(file_nameparts) > 1:
        for format in formats:
            last_part = file_nameparts[-1]
            if format == last_part:
                return format      
    return "application/octet-stream"

assert "zip" == print_format("jpeg.exe.zip")
assert "application/octet-stream" == print_format("jpeg.exe")
assert "txt" == print_format("prices.txt")
assert "application/octet-stream" == print_format("jpeg")
assert "jpg" == print_format("screenshot.jpg")
assert "jpeg" == print_format("franken.jpeg")
assert "application/octet-stream" == print_format("application/octet-streamprint_format")
print("success")