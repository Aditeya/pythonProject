#!/usr/bin/env python

import opc
import winsound
# Play Windows exit sound.
winsound.Beep(440, 200)
winsound.PlaySound("Rainbow.mp3", winsound.SND_FILENAME)
