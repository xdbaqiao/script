#!/bin/bash
#>_<, ^_^, T_T, $_$, (￣﹁￣), ^(oo)^

file=/home/yexinjing/.zshrc
output_file=/tmp/zshrc.tmp

face=('>_<' '\^_\^' 'T_T' '\$_\$' '(￣﹁￣)' '\^(oo)\^')


if [ ! $1 ];then
    let num=$(($RANDOM % 6))
    chg=${face[$num]}
else
    echo 'Error.'
    exit
    #chg='$1'
fi

echo $chg

for i in `seq 6`;
do
    sig=${face[$i-1]}
    cat "$file" |grep "$sig" >/dev/null
    if [ $? -eq 0 -a "$sig" ];then
        tmp='s/'"$sig"'/'$chg'/'
        echo $tmp
        sed -e $tmp $file > $output_file
        if [ $? -eq 1 ];then
            break
        fi
        rm $file
        cp $output_file $file
        break
    fi
done
