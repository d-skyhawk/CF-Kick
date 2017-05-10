
g++ main.cpp

read total < "testcases"

flag=0

for ((idx=1;idx<=total;idx++))
	do
		tt="test"
		tt="$tt$idx"
		ans="ans"
		./a.out < $tt > $ans
		ax="soln$idx"
		if diff -w "$ax" "$ans" >/dev/null
			then
			echo "Test $idx Passed"
		else
			echo "Test $idx Failed"
			flag=1
		fi
done

if [ $flag -eq 1 ]
	then
	echo "Not all Cases Passed"
else
	echo "You are a Stud"
fi