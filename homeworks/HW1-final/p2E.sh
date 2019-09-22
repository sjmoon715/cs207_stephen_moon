for f in $( ls); do
	if [ -f $f ]; then
		lines=$(wc -l < $f)
		echo $f $lines 	
	fi
done
