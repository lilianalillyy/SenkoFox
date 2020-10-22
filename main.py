import glob
import os
import shutil

# Specify your Firefox Install Path
# /usr/lib/firefox is OS-specific (in my case Linux),
# however the rest should be the same regardless of a system.
# Windows users however use "\" instead of "/"!
firefoxIconsPath = "/usr/lib/firefox/browser/chrome/icons/default"

# Path to the Senko icon. By default in this folder
senkoFoxPath = "icon"

# Run
path = os.path.join(firefoxIconsPath, "*.png")
firefox = glob.glob(path);

for ico in firefox:
  print("Unlinking", ico)
  os.unlink(ico)

  icon = os.path.join(senkoFoxPath, os.path.basename(ico))

  print(icon + " -> " + ico)
  shutil.copy2(icon, ico)