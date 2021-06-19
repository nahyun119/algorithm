function cal(mode){
    var funcs = {
        'plus' : function(left, right){
            return left + right;
        }
    }
    return funcs[mode];
}


console.log(cal('plus'));