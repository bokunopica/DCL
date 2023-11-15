import json
import random

def preprocess_openi_zh_pa(save_dir):
    data_dir = "/home/qianq/data/OpenI-zh"
    image_dir = f"{data_dir}/images"
    ann_dir = f"{data_dir}/openi-zh.json"
    with open(ann_dir, 'r') as f:
        ann = json.loads(f.read())['annotations']
        # data_list = os.listdir(image_dir)

    result_list = []
    for item in ann:
        result_list.append({
            "image_path": f"{image_dir}/{item['image_id']}.png",
            "report": item['caption'],
            "triplets": []
        })

    random.shuffle(result_list)
    total_len = len(result_list)
    train_len = int(0.8 * len(result_list))
    test_len = int((total_len - train_len)*0.5)
    # val_len = total_len - train_len - test_len
    
    result_dict = {
        "train": result_list[:train_len],
        "test": result_list[train_len:train_len+test_len],
        "val": result_list[train_len+test_len:]
    }
    
    
    with open(save_dir, 'w') as f:
        f.write(json.dumps(result_dict, ensure_ascii=False))


if __name__ == "__main__":
    preprocess_openi_zh_pa('annotations/openi_zh.json')
