# file_extractor
Command line interface for searching and extracting files out of large directories.

## Usage
![](extractor_example.gif)

### copy
This argument will copy all the interested files from the source directory to the final directory without maintaining the original file hierarchy.

### move
This argument will move (cut) all the interested files from the source directory to the final directory without maintaining the original file hierarchy.

### categories
- `common_media`
  - Extensions often used to store personal photos and videos 
  - Includes jpg, jpeg, mp4, mov, wmv, and avi.
- `images`
  - Includes jp2, jfi, jpeg, jpm, bmp, png, tif, webp, dib, j2k, mj2, jpe, heif, jfif, jpf, heic, k25, cr2, gif, arw, raw, jif, jpg, nrw, tiff, and jpx.
- `vector`
  - Includes svg, eps, pdf, ai, and svgz.
- `videos`
  - Includes swf, wmv, dixv, flv, mov, h264, avi, qt, h265, mpeg4, xvid, mj2, mp4, mkv, and avchd.
- `audio`
  - Includes aif, aac, flac, aiff, wav, wma, mp4, m4a, pcm, snd, mp3, and aifc.
- `documents`
  - Includes xls, pptx, doc, xlsx, pdf, csv, and docx.
