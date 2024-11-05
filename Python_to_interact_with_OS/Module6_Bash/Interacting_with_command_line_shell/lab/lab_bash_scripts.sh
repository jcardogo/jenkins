if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
echo "I am appending text to this test file" >> test.txt
for i in 1 2 3; do echo $i; done