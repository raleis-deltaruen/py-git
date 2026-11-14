

formats = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
def print_format(file: str) -> str:
    result = file
    for format in formats: 
        if result.endswith("." + format):
            return format      
    return "application/octet-stream"

assert "application/octet-stream" == print_format("jpeg")
assert "txt" == print_format("prices.txt")
assert "jpg" == print_format("screenshot.jpg")
assert "jpeg" == print_format("franken.jpeg")
assert "application/octet-stream" == print_format("application/octet-stream")
print("success")