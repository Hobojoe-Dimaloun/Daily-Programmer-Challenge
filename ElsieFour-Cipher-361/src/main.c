#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *decrypt(char *message, char *encryptKey);

char *refKey="#_23456789abcdefghijklmnopqrstuvwxyz";
int keyLength = 36;
int messagelen = 100;

int main(int argc, char* argv[])
{

//char encryptKey[keyLength+1];
//	char message[messagelen+1];

	char *encryptKey = "s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b";
	char *message = "tk5j23tq94_gw9c#lhzs";
	printf("Encryption key\n" );
	//fgets(encryptKey,keyLength+1,stdin);
	printf("Message key\n" );
	getchar();
	//fgets(message,messagelen+1,stdin);



	printf("%s",decrypt(message, encryptKey));


	return 0;
}


char *decrypt(char *message, char *encryptKey)
{
	char marker = encryptKey[0];
	char *decryptMsg=calloc(messagelen,sizeof(*decryptMsg));
	for(int i = 0; i<strlen(message); i++)
	{
		int markNum, leftShift, upShift;
		int charNum,messNum;

		// get the marker and message character numbers
		for(int j = 0; j<strlen(refKey);j++)
		{
			if(marker == refKey[j])
			{
				markNum=j;
			}
			if(message[i] == refKey[j])
			{
				charNum=j;
			}
			if(message[i] == encryptKey[j])
			{
				messNum=j;
			}
		}

		// Work out shift for the cipher to plain
		leftShift = 6-markNum%6;
		upShift = 6-markNum/6;

		// location of message char in cipher array
		int coordx = messNum%6;
		int coordy = (messNum-coordx)/6;
		// location of dycrpt in array
		int x = (coordx + leftShift)%6;
		int y = (coordy + upShift)%6;
		decryptMsg[i] = encryptKey[6*y+x];
		printf("%d\n",y);
		// store end result
		char temp = encryptKey[6*y+5];
		// rotate row with plain text in
		for(int column = 5; column > 0; column--)
		{
			encryptKey[6*y+column] = temp; //encryptKey[6*y + (column -1)%6];
		}
		//encryptKey[6*y] = temp;

	/*	temp = encryptKey[x];
		for(int row = 5; row >=0; row--)
		{
			encryptKey[6*row + x] = encryptKey[6*(row-1)%6 + x ];
		}
		encryptKey[6*5 + x] = temp;
	/*	int plainNum;
		for(int j = 0; j<strlen(refKey);j++)
		{

			if(decryptMsg[i] == refKey[j])
			{
				plainNum=j;
			}
		}
	/*	markShiftright = -plainNum%6;
		markShiftDown = -plainNum/6;

		markCoordx =
		markCoordy

		marker = encryptKey[]*/
	}
	return decryptMsg;
}
