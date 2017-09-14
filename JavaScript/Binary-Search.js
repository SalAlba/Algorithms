function x(arr, item){
    var low = 0;
    var heigh = arr.length - 1;
	  var i=1;
    while( low <= heigh ){
        var med = Math.floor((low + heigh) / 2);
		console.log('iter : '+i++);
        if( arr[med] == item )
            return med;
        else if(arr[med] < item)
            low = med +1;
        else 
            heigh = med -1;
    }
    return null;
}
