
```

An attempt to use DeepLearning to decode the file encryptions

Four Types of Encryptions has been chosen for the project

1: Replacement Encryption -> It's a simple encryption like a ceaser cipher, its replaces the characters with some numbers as shown,


sports	198041105120189020701980
tehnounion	2070522081902130512021602130918051202130
ruusan	189021602160198012602130
dsc00824	42301980324011111111999933335555
desc	4230522019803240
vixy	2230918024302520
kapcsolat	616012604110324019805120815012602070
smooth	198091405120512020708190
steve	19802070522022305220
prediction	4110189052204230918032402070918051202130



2: Simple Encryption      -> It's an encryption which uses 16 digit pattern code as shown,  



test	1000000010108001100000100015000110000001010100011000000010101001
curtas	100011400000000110000000010106011000001010400001100000001010200110000000001180011000000101020001
arroz	10000000001110011000001010500001100000101060000110010101000000011000010011000001
jewelry	1000000011600001100000100012000110100130000000011000001000130001100000000001170110000010102000011000100130000001
gardens	1001120000000001100000000011400110000010103000011113000000000001100000100014000110101030000000011000000101040001
thuna	10000000101050011000011800000001100000000101070110101040000000011000000000115001
lineatv	1000000000011801100000114000000110101050000000011000001000150001100000000011600110000000101060011100120000000001



3: Encryption with key    -> It's an encryption which uses key with 16 digit pattern code as shown,



test	9000117293351009900011828337500990001173843150099000117293352009
curtas	900023128324500990001172842557099000118294045009900011729335300990001172833630099000117384325009
arroz	90001172833560099000118293345009900011829344500990011277832450099000127299245009
jewelry	9000117294545009900011828342500990101302832450099000118283355009900011728325630990001182938450099000217423245009
gardens	9001257283245009900011728335900990001182939450099118117283245009900011828336500990102192832450099000117384265009
thuna	90001172933480099000128383245009900011728425580990102202832450099000117283360009
lineatv	9000117283256409900011840324500990102212832450099000118283375009900011728336100990001172933490099100287283245009



4: Complex Encryption     -> It's an encryption which has key with 16 digit pattern code, along with the rotation of keys as shown,



test	9002127383245009900042728424500990004182932450099003127383245009
curtas	900011729135500990702182832450099000177384245009900412738324500990052272832450099000518293245009
arroz	90062272832450099000187384245009900019738424500990001173633460099000118383345009
jewelry	9000178383245009900092728424500990001172853451099000227284245009905121728324500990001573842450099000117593255009
gardens	9000117283356009900122728324500990001673842450099000117283246119900032728424500990001172912551099000718293245009
thuna	90071273832450099000117364345009908021828324500990001172842551099002227283245009
lineatv	9061217283245009900011779424500990001172852551099000427284245009900322728324500990081273832450099000117283355019



All these encryptions are specifically written for this project.


The training has given to neural networks with different parameters and architectures, 
Results found that these models are not able to find the patterns how the encryption has been done.
Encryption data is statistically indistinguishable from randomness. 
Machine learning is generally based on discovering statistical patterns in the data, 
if data is random, models will not be able to find the patterns.


if there is large amount of randomness it becomes more difficult to decrypt the data.
We need more computational power and architecture to train more complex encryptions, 
we may come closer to the actual values that purely depends upon the computational power and architecture of model.

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

[open folder](https://drive.google.com/drive/folders/1xGZkXXCtq9wnM73_QjH5siNOFczqZMsa?usp=sharing)


This is purely a capability of DeepLearning Models, we may achieve this with further advancement in the field of AI.

```
