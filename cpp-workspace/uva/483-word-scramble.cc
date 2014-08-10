#include <iostream>
#include <cstdio>
#include <cctype>

#define BUFSIZE 1 << 21

char buf[BUFSIZE];

using namespace std;

void reverse_word(int start, int end) {
	while (start < end) {
		char t = buf[start];
		buf[start++] = buf[end];
		buf[end--] = t;
	}
}

int main() {
	int count = fread(buf, sizeof(char), BUFSIZE, stdin);
	buf[count] = '\0';	// sentinel, not printed
	int l = 0, r = 0;
	for (int i = 0; i <= count; i++) {
        /*
            p c
            0 0 r++, i++
            0 1 i++
            1 0 call(l, r-1), l = i, i++, r++
            1 1 i++

            p := r < i
            c := ith char is whitespace
         */
		if (!isspace(buf[i])) {
			if (r < i) {
				reverse_word(l, r - 1);
				l = i;
			}
			r = i + 1;
		}
	}

	fwrite(buf, sizeof(char), count, stdout);
	return 0;
}
