read -r -p "Pick a file to commit: " fadd
git add $fadd
git status
read -r -p "Confirm your selection (Y or N) " cant
if [ "$cant" = "N" ]; then
	echo "Canceled"
	exit 1
fi
echo "OK"
read -r -p "Commit message: " mess
git commit -m "$mess"
git status
read -r -p "Do you wish to finalize your commit? " cant
if [ "$cant" = "N" ]; then 
        echo "Canceled"
        exit 1
fi
git push
