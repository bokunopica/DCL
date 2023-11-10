import json
import os

def preprocess_openi_zh_pa(save_dir):
    data_dir = "/home/qianq/data/OpenI-zh"
    image_dir = f"{data_dir}/images"
    ann_dir = f"{data_dir}/openi-zh.json"
    with open(ann_dir, 'r') as f:
        ann = json.loads(f.read())['annotations']
        data_list = os.listdir(image_dir)

    result_list = []
    for item in ann:
        result_list.append({
            "image_path": f"{image_dir}/{item['image_id']}.png",
            "report": item['caption'],
        })
    
    with open(save_dir, 'w') as f:
        f.write(json.dumps(result_list, ensure_ascii=False))


if __name__ == "__main__":
    preprocess_openi_zh_pa('annotations/openi_zh.json')
