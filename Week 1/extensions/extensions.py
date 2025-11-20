def main():
    extensionName = input("File name: ").lower()

    if ".gif" in extensionName:
        print("image/gif")

    elif ".jpg" in extensionName:
        print("image/jpeg")

    elif ".jpeg" in extensionName:
        print("image/jpeg")

    elif ".zip" in extensionName:
        print("application/zip")

    elif "pdf" in extensionName:
        print("application/pdf")

    elif ".png" in extensionName:
        print("image/png")

    elif ".txt" in extensionName:
        print("text/plain")

    else:
        print("application/octet-stream")

main()
