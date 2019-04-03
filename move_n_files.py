from pathlib import Path
from shutil import copy2

def move_n_files(source_path, des_path):
    print("Start!")
    s_path = Path(source_path)
    d_path = Path(des_path)

    audio_path = s_path / f"audio"
    video_path = s_path / f"video"

    audio_ind = [a for a in audio_path.glob("*.wav") if a.is_file()]
    video_ind = [v for v in video_path.glob("*.mpg") if v.is_file()]

    for i in range(0,800):
        copy2(str(f"{audio_ind[i]}"), str(d_path / f"grid_s2_train"/ f"train" / f"audio")) 
        copy2(str(f"{video_ind[i]}"), str(d_path / f"grid_s2_train"/ f"train" / f"video")) 
    for i in range(800,900):
        copy2(str(f"{audio_ind[i]}"), str(d_path / f"grid_s2_val"/ f"val" / f"audio")) 
        copy2(str(f"{video_ind[i]}"), str(d_path / f"grid_s2_val"/ f"val" / f"video")) 
    for i in range(900,1000):
        copy2(str(f"{audio_ind[i]}"), str(d_path / f"grid_s2_test"/ f"test" / f"audio")) 
        copy2(str(f"{video_ind[i]}"), str(d_path / f"grid_s2_test"/ f"test" / f"video")) 
    print("Done!")

if __name__ == "__main__":
    move_n_files("/media/datas-2/steinsun/datasets/grid/s2/", "/media/datas-2/steinsun/datasets/grid_s2/")