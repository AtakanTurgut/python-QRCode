import qrcode

img = qrcode.make('https://open.spotify.com/playlist/37i9dQZF1DX9stbPFTxeaB?si=69a8a0fa56ca4ecc')

img.save('iLoveThisPlaylist.jpg')
