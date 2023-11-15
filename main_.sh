CUDA_VISIBLE_DEVICES=0 python main.py \
    --config ./configs/BLIP.yaml \
    --output_dir output/Generation \
    --dataset_name openi_zh \
    --distributed False \
    --batch_size 8 \
    --epochs 50 \
    --save_dir results/test \
    --bert sci \
    --image_dir /home/qianq/data/OpenI-zh/images \
    --knowledge_path /home/qianq/mycodes/DCL/annotations/openi_zh.json \
    --ann_path /home/qianq/mycodes/DCL/annotations/openi_zh.json \
    --task None
    
    # --master_port=21073 \