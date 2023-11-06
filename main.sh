CUDA_VISIBLE_DEVICES=0,1,2,3 TORCH_DISTRIBUTED_DEBUG=DETAIL python -m torch.distributed.run \
    --nproc_per_node=2 \
    main.py \
    --config ./configs/BLIP.yaml \
    --output_dir output/Generation \
    --dataset_name openi_zh \
    --distributed False \
    --batch_size 8 \
    --epochs 50 \
    --save_dir results/test \
    --bert sci
    # --master_port=21073 \