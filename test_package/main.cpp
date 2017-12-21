#include <JlCompress.h>
 
int main(int argc, char * argv[])
{
	JlCompress::compressFile("C:/test.zip", "C:/test.txt");
	JlCompress::extractDir("C:/test.zip", "C:/");
	return 0;
}