#!/bin/bash
export DATA_DIR=data_dir
export TF_XLA_FLAGS="" #--tf_xla_cpu_global_jit
python run_classifier.py --do_train=False \
    --bert_config_file=$DATA_DIR/bert_large_config.json \
      --vocab_file=$DATA_DIR/github_python_minus_ethpy150open_deduplicated_vocabulary.txt \
        --task_name=exception \
	  --init_checkpoint=$DATA_DIR/exception__epochs_20__pre_trained_epochs_1/model.ckpt-378 \
	    --data_dir=$1 \ #$DATA_DIR/pred_exception_datasets \
	      --output_dir=$2 \ #pred_exception_results \
	        --do_eval=False --do_predict=True
