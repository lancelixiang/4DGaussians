/home/ubuntu/lance/4DGaussians/arguments/__init__.py
L59 后缀

``` python
python train.py -s data/dnerf/bouncingballs --port 6017 --expname "dnerf/bouncingballs" --configs arguments/dnerf/bouncingballs.py 
python render.py --model_path "output/dnerf/bouncingballs/"  --skip_train --configs arguments/dnerf/bouncingballs.py 
```


``` python
python train.py -s myData/satellite --port 6017 --expname "dnerf/satellite" --configs arguments/dnerf/satellite.py 
python render.py --model_path "output/dnerf/satellite/"  --skip_train --configs arguments/dnerf/satellite.py 
```