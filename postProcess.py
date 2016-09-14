# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:41:50 2016

@author: dahoiv
"""

import os
import util

if __name__ == "__main__":
    os.nice(19)
    if False:
        import do_img_registration_LGG_POST as do_img_registration
        util.setup("LGG_POST_RES/", "LGG")
    elif False:
        import do_img_registration_LGG_PRE as do_img_registration
        util.setup("LGG_PRE_RES/", "LGG")
    elif True:
        import do_img_registration_GBM as do_img_registration
        util.setup("GBM_RES2/", "GBM")

    if not os.path.exists(util.TEMP_FOLDER_PATH):
        os.makedirs(util.TEMP_FOLDER_PATH)

    if True:
        util.post_calculations_qol()
    else:
        image_ids = do_img_registration.find_images()
        util.post_calculations(image_ids)
