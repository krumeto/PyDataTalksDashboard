import os
from googleapiclient.discovery import build
import pandas as pd

API_KEY = os.environ.get('YOUTUBE_API')

youtube = build('youtube', 'v3', developerKey = API_KEY)

pychannels = [('PyDataTV', 'UCOjD18EJYcsBog4IozkF_7w'), ('EnthoughtMedia', 'UCkhm72fuzkS9fYGlGpEmj7A'), ('Google Cloud Platform', 'UCJS9pqu9BzkAMNTmzNMNhvg',),
('PyData Montreal','UC2d_azMgPLw_8JzgbpNb2oQ'), ('Anaconda, inc.', 'UCND4vKhJssAtK8p1Blfj14Q'), ('PyDataMCR','UCTCV2vonJgaQVb8AdMgdvCA'), ('PyData Madison','UCR3LMPeZR_VcaIAj_YnR_sw'),
('PyData São Paulo', 'UCejuzULiRcqml_DOnY2IFfA' ), ('PyCon 2019', 'UCxs2IIVXaEHHA4BtTiWZ2mQ'), ('PyCon 2020', 'UCMjMBMGt0WJQLeluw6qNJuA'), ('PyCon 2017', 'UCrJhliKNQ8g0qoE_zvL8eVg'),
('PyCon 2018', 'UCsX05-2sVSH7Nx3zuk3NYuQ'), ('PyCon 2015', 'UCgxzjK6GuOHVKR_08TT4hJQ'), ('PyCon 2016', "UCwTD5zJbsQGJN75MwbykYNw"), ('PyCon Israel', 'UC-SbPEAZ4Ik2cowdR_Wyfag'),
('PyCon 2014', 'UCFDHJGm0IxH9uwcIHfR72yg'), ('PyCon Sweden', 'UCH_2cuWzFMyCPvm75lJJ6wg'), ('PyCon UK', 'UChA9XP_feY1-1oSy2L7acog'), ('PyCon South Africa', 'UCu-El65PtQm46aSbXkzykYQ'),
('PyCon Canada', 'UCclkPrurwUP_ajqi3vDTNDg'), ('PyCon CZ', 'UCRC2Vu7p4SJxhhuRdl8rQ6g'), ('EuroPython Conference', 'UC98CzaYuFNAA_gOINFB0e4Q'),('PyConDE', 'UCji5VWDkGzuRenyRQZ9OpFQ'),
('PyCon Taiwan', 'UCHLnNgRnfGYDzPCCH8qGbQw'), ('PyConAU', 'UCS9sdEyduD9K83K3GkvQlOA'), ('PyCon Korea', 'UC26x6D5xpKx6io4ShfXa_Ow'), ('PyCon Thailand', 'UCtHekbmBXtp5AYSVARFQQiw'), 
('theuapycon', 'UCLTojVNHUm8KfpEOq_b36QA'), ('PyCon Balkan', 'UC4Zfal_sduHM2sIT5Mm9cJA'), ('PyCon Colombia', 'UCjor6U0ZF5zGAYLJJt9gr0A'), ('PyCon PL', 'UChSapCUgd_L5nBWIqWucnnQ'),
('pyconitalia', 'UCOyJ9ritUBmjXhoRXOFahJA'), ('PyCon SK', 'UC8Tzn82aG4zdvtqlrfsLgSA'), ('PyCon Zimbabwe', 'UCUIWWO9HgKw3-tjrY0jeU_w'), ('PyCon Ukraine', 'UCJ2lwx-pNVF_EoWlHAmNNtQ'),
('PyConJP', 'UCxNoKygeZIE1AwZ_NdUCkhQ'), ('PyCon Nigeria', 'UCXq7L06VgQ04xFHFG_qFh5A'), ('PyCon Hong Kong', 'UCQJEx-ZrVjpB7dYWnO4EecA'), ('PyCon SG', 'UCdlxRI--Br1YNdz95U97jeg'),
('PyCon Indonesia', 'UCki_EPDl9JRVfVVkntNdJLA'), ('PyCon Tanzania', 'UCVaRe-jaUZH4ajleOiWN8vQ'), ('PyCon India', 'UCVxPTRxEcoWjEFIMXHaGgHA'), ('PyAr', 'UCjYLIv07fw21w0uIAtUMnNA'),
('PyCon Latam', 'UCS2Qt4mzoogx6bTNZ4GXZkQ'), ('PyCon Apac', 'UCVN315m23vfiVuU4Ov51tDw'), ('PyCon India 2018', 'UCqzv3lvF6fYxPRvSfWcJXdg'), ('PyCon España', 'UCyth_6hqft9a7B_thdwYyww'),
('PyCon China', 'UC6wdANyncX4Bc59wTVKrUlw'), ('PyData Salamanca', 'UCqVNbNRMMjuuwRAJwnVIuvw'), ('PyData Krakow', 'UCpha908Cb_1ykkFK7G8M4yA') , ('PyData Bristol', 'UCLx854lMH98BpyVfi-bnQkw'), 
('PyData.Osaka', 'UCXHrkobjEf1yLkmblB6CHyg'), ('PyData Warsaw', 'UCNl5PC05Wm7GyzR7NkZoxZw'), ('PyData Bydgoszcz',"UCe2iuKW4GLjR837xp-ERETQ"), ('PyData Pune','UCEnagt088yX-ruTalg-GJeQ'), 
('PyData Taipei', 'UC-sYXndx7shbVqOBqH4BbdQ'), ('PyData Manipal', 'UCUnU4bzivbG1EaJApxhhA1g'), ('San Francisco PyData Meetup Group', 'UC34--jrgq8QvMs8Jt_kro3w'), ('PyData Mumbai', 'UCawiaZaabJLXV7IL_IF3M4Q'),
('PyData Eindhoven', 'UC1rImWhf9mv6p5ZbGc5dRHA'), ('PyData Copenhagen', 'UCphaUFghyyhpd9Fi2nBKsNA'),  ('PyData Bangalore', 'UC8D_q-ZIxMtCy0ClWN1nfUw'), ('Georgi Karadzhov', 'UC4GNSALq9obnCMYWq32tNmQ'),
('PyData Lancaster', 'UCdgx_UhyKcy2V0dkKwBGVEQ'), ('PyData Tokyo', 'UCwvss5yZK7xJWT46m1DhyFg'), ('PyData Brasilia', 'UCFXlV7l3u237Y-xQ-2YQzAA'), ('SciPyLA', 'UClb88lwUvlFikmhTzVGsVGA'), 
('EuroSciPy', 'UCruMegFU9dg2doEGOUaAWTg'),  ('Kaggle','UCSNeZleDn9c74yQc-EKnVTA'),  ('Explosion', 'UCFduT4kW_eLDbEW6XoA5F0A')]

channel_request = youtube.channels().list(
    part = 'contentDetails',
    forUsername = "kaggledotcom"
    #id = "UCphaUFghyyhpd9Fi2nBKsNA"
    #id = 'UCOjD18EJYcsBog4IozkF_7w'

)

channel_response = channel_request.execute()
print(channel_response)

channels_df = pd.DataFrame(pychannels, columns = ('channel_name', 'channel_id'))

print(channels_df.shape)
print(channels_df.head())
