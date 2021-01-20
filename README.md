
```

An attempt to use DeepLearning to decode the file encryptions

Four Types of Encryptions has been chosen for the project

1: Replacement Encryption
It's a simple encryption like a ceaser cipher, its replaces the characters with some numbers as shown,


sports	198041105120189020701980
tehnounion	2070522081902130512021602130918051202130
ruusan	189021602160198012602130


2: Simple Encryption  
It's an encryption which uses 16 digit pattern code as shown,  



test	1000000010108001100000100015000110000001010100011000000010101001
curtas	100011400000000110000000010106011000001010400001100000001010200110000000001180011000000101020001
arroz	10000000001110011000001010500001100000101060000110010101000000011000010011000001



3: Encryption with key     
It's an encryption which uses key with 16 digit pattern code as shown,



test	9000117293351009900011828337500990001173843150099000117293352009
curtas	900023128324500990001172842557099000118294045009900011729335300990001172833630099000117384325009
arroz	90001172833560099000118293345009900011829344500990011277832450099000127299245009



4: Complex Encryption     
It's an encryption which has key with 16 digit pattern code, along with the rotation of keys as shown,



test	9002127383245009900042728424500990004182932450099003127383245009
curtas	900011729135500990702182832450099000177384245009900412738324500990052272832450099000518293245009
arroz	90062272832450099000187384245009900019738424500990001173633460099000118383345009



All these encryptions are specifically written for this project.


The training has given to neural networks with different parameters and architectures, 
Results found that these models are not able to find the patterns how the encryption has been done.
Encryption data is statistically indistinguishable from randomness. 
Machine learning is generally based on discovering statistical patterns in the data, 
if data is random, models will not be able to find the patterns.


if there is large amount of randomness it becomes more difficult to decrypt the data.
We need more computational power and architecture to train more complex encryptions, 
we may come closer to the actual values that purely depends upon the computational power 
and architecture of model.

Loss functions will move from infinity to min value possible and after finding a max possible min value,
the loss function doesnot show any dip to minimum value(zero),
the predictions may be closely related to actual values or may not depends on randomness of input data.


If encrypitons are simple we can come closer to the solution, 
as we have successfully decrypted the  "Replacement Encryption"



Model summary, which is used for training of "Replacement Encryption" data

Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 2100)              4200      
_________________________________________________________________
dense_1 (Dense)              (None, 1750)              3676750   
_________________________________________________________________
dense_2 (Dense)              (None, 1400)              2451400   
_________________________________________________________________
dense_3 (Dense)              (None, 1050)              1471050   
_________________________________________________________________
dense_4 (Dense)              (None, 700)               735700    
_________________________________________________________________
dense_5 (Dense)              (None, 350)               245350    
_________________________________________________________________
dense_6 (Dense)              (None, 1)                 351       
=================================================================
Total params: 8,584,801
Trainable params: 8,584,801
Non-trainable params: 0


"Loss function used : MAE -> 1.1 (error)"

xtest       -> ant
ytest       -> 126121302070
ypred       -> ant

This model predicts correct values for some data and may predicts wrong for some data, 
this is due to error present in Loss(MAE) during training.

Providing below the drive link which contains notebook used for training and trained model in h5 format
```

[open folder for training and trained model in h5 format](https://drive.google.com/drive/folders/1xGZkXXCtq9wnM73_QjH5siNOFczqZMsa?usp=sharing)

```

This is purely a capability of DeepLearning Models, 
we may achieve this with further advancement in the field of AI.

```
