import typer

extension_dict = {
    # Programming languages
    "py":"Try looking into the file: cat {file}", "cpp":"Try looking into this file: cat {file}", "c":"Try looking into this file: cat {file}", "js": "Try looking into this file: cat {file}", "html": "Try looking into this file: cat {file}",

    # Pcap files
    "pcap":"A pcap file: a network file: try using wireshark.", "pcapng":"A pcap file: a network file: try using wireshark",

    # All zip files
    "zip":"This is a compressed file, try unzip or zipinfo, if you need more tooling (binwalk, maybe exiftool)", "tar.gz":"This is a compressed file: try unzip or zipinfo.",

    # Pictures
    
    "png":"This is a image, you can run exiftool {file}, binwalk {file}, or strings {file} | less",
    "":"",

    # Disk images
    "img":"A disk image"
    

}

app = typer.Typer()

@app.command()
def look(file: str):
    try:
        file_splitted = file.split(".")
        extension = file_splitted[1]
        if extension in extension_dict:
            print(f"{extension_dict[extension]}")
        else:
            print(f"This file type is not in the database, try running file {file}")
        
    except:
        print("There is no extension: try running:")
        print(f"file {file}")


if __name__ == "__main__":
    app()
