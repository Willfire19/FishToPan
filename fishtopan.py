# Python script to convert FishEye shots to panoramic pictures for 3d use
from PIL import Image
import math
import sys

print "Fish To Panorama!"

img = Image.open('NFLCoinToss.jpg')
# print img
# img.show()

# assume the src image is square, and its width has even num of pixels
length = img.width / 2
height = img.height
print "Length: " + str(length)
print "Height: " + str(height)

imDest = Image.new("RGB", (4 * length, height) )
imBilinear = Image.new("RGB", (4 * length, height) )

for i in range(0, imDest.height/2):
# for i in range(imDest.height/2, imDest.height):
	for j in range(0, imDest.width):

		radius = float(length - i)
		# theta = 2.0 * math.pi * float(4.0 * length - j) / float(4.0 * length)
		theta = 2.0 * math.pi * float(-j) / float(4.0 * length)
		# theta = 2.0 * math.pi * float(-j) / float(4.0 * length)


		fTrueX = radius * math.cos(theta)
		fTrueY = radius * math.sin(theta)

		# "normal" mode
		x = int( (round(fTrueX)) + length )
		y = length - int( (round(fTrueY)) )

		# check bounds
		if x >= 0 and x < (2 * length) and y >= 0 and y < (2 * length):
			if "--flip" in sys.argv:
				imDest.putpixel( (j, imDest.height/2 - i), img.getpixel( (x, y) ) )
			else:
				imDest.putpixel( (j, i), img.getpixel( (x, y) ) )
			# imDest.putpixel( (j, imDest.height/2 - i), img.getpixel( (x, y) ) )
			# imDest.putpixel( (j, i), img.getpixel( (x, y) ) )
			# imDest[j, i] = img.getpixel((x, y))

imDest.show()

imDest.save("NFLCoinTossPan.jpg", "JPEG")


# // assume the source image is square, and its width has even number of pixels
# Bitmap bm = new Bitmap("lillestromfisheye.jpg");
# int l = bm.Width / 2;
# Bitmap bmDestination = new Bitmap(4 * l, l);
# Bitmap bmBilinear = new Bitmap(4 * l, l);
# int i, j;
# int x, y;
# double radius, theta;

# // for use in neighbouring indices in Cartesian coordinates
# int iFloorX, iCeilingX, iFloorY, iCeilingY;
# // calculated indices in Cartesian coordinates with trailing decimals
# double fTrueX, fTrueY;
# // for interpolation
# double fDeltaX, fDeltaY;
# // pixel colours
# Color clrTopLeft, clrTopRight, clrBottomLeft, clrBottomRight;
# // interpolated "top" pixels
# double fTopRed, fTopGreen, fTopBlue;
# // interpolated "bottom" pixels
# double fBottomRed, fBottomGreen, fBottomBlue;
# // final interpolated colour components
# int iRed, iGreen, iBlue;

# for (i = 0; i < bmDestination.Height; ++i)
# {
# 	for (j = 0; j < bmDestination.Width; ++j)
# 	{
# 		radius = (double)(l - i);
# 		// theta = 2.0 * Math.PI * (double)(4.0 * l - j) / (double)(4.0 * l);
# 		theta = 2.0 * Math.PI * (double)(-j) / (double)(4.0 * l);

# 		fTrueX = radius * Math.Cos(theta);
# 		fTrueY = radius * Math.Sin(theta);

# 		// "normal" mode
# 		x = (int)(Math.Round(fTrueX)) + l;
# 		y = l - (int)(Math.Round(fTrueY));
# 		// check bounds
# 		if (x >= 0 && x < (2 * l) && y >= 0 && y < (2 * l))
# 		{
# 			bmDestination.SetPixel(j, i, bm.GetPixel(x, y));
# 		}

# 		// bilinear mode
# 		fTrueX = fTrueX + (double)l;
# 		fTrueY = (double)l - fTrueY;

# 		iFloorX = (int)(Math.Floor(fTrueX));
# 		iFloorY = (int)(Math.Floor(fTrueY));
# 		iCeilingX = (int)(Math.Ceiling(fTrueX));
# 		iCeilingY = (int)(Math.Ceiling(fTrueY));

# 		// check bounds
# 		if (iFloorX < 0 || iCeilingX < 0 ||
# 			iFloorX >= (2 * l) || iCeilingX >= (2 * l) ||
# 			iFloorY < 0 || iCeilingY < 0 ||
# 			iFloorY >= (2 * l) || iCeilingY >= (2 * l)) continue;

# 		fDeltaX = fTrueX - (double)iFloorX;
# 		fDeltaY = fTrueY - (double)iFloorY;

# 		clrTopLeft = bm.GetPixel(iFloorX, iFloorY);
# 		clrTopRight = bm.GetPixel(iCeilingX, iFloorY);
# 		clrBottomLeft = bm.GetPixel(iFloorX, iCeilingY);
# 		clrBottomRight = bm.GetPixel(iCeilingX, iCeilingY);

# 		// linearly interpolate horizontally between top neighbours
# 		fTopRed = (1 - fDeltaX) * clrTopLeft.R + fDeltaX * clrTopRight.R;
# 		fTopGreen = (1 - fDeltaX) * clrTopLeft.G + fDeltaX * clrTopRight.G;
# 		fTopBlue = (1 - fDeltaX) * clrTopLeft.B + fDeltaX * clrTopRight.B;

# 		// linearly interpolate horizontally between bottom neighbours
# 		fBottomRed = (1 - fDeltaX) * clrBottomLeft.R + fDeltaX * clrBottomRight.R;
# 		fBottomGreen = (1 - fDeltaX) * clrBottomLeft.G + fDeltaX * clrBottomRight.G;
# 		fBottomBlue = (1 - fDeltaX) * clrBottomLeft.B + fDeltaX * clrBottomRight.B;

# 		// linearly interpolate vertically between top and bottom interpolated results
# 		iRed = (int)(Math.Round((1 - fDeltaY) * fTopRed + fDeltaY * fBottomRed));
# 		iGreen = (int)(Math.Round((1 - fDeltaY) * fTopGreen + fDeltaY * fBottomGreen));
# 		iBlue = (int)(Math.Round((1 - fDeltaY) * fTopBlue + fDeltaY * fBottomBlue));

# 		// make sure colour values are valid
# 		if (iRed < 0) iRed = 0;
# 		if (iRed > 255) iRed = 255;
# 		if (iGreen < 0) iGreen = 0;
# 		if (iGreen > 255) iGreen = 255;
# 		if (iBlue < 0) iBlue = 0;
# 		if (iBlue > 255) iBlue = 255;

# 		bmBilinear.SetPixel(j, i, Color.FromArgb(iRed, iGreen, iBlue));
# 	}
# }

# bmDestination.Save("fisheyelandscape.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
# bmBilinear.Save("fisheyebilinearlandscape.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);