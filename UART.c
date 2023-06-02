/*
 * reception_uart.c
 *
 *  Created on: 5 juin 2019
 *      Author: stage
 */

#include "reception_uart_CT.h"

void reception_uart (u8 RecvBuffer[]){

	int ReceivedCount;

		ReceivedCount = 0;
		while (ReceivedCount < TEST_BUFFER_SIZE && RecvBuffer[ReceivedCount-1] != '!' ) {
			ReceivedCount +=
				XUartPs_Recv(&Uart_Ps, &RecvBuffer[ReceivedCount],
						  (TEST_BUFFER_SIZE - ReceivedCount));
			if (ReceivedCount > 0 && RecvBuffer[0] == '\r') {
			            // Supprimer le caractère '\r' du début de la chaîne
			            memmove(RecvBuffer, RecvBuffer + 1, ReceivedCount - 1);
			            ReceivedCount--;
			        }
		}

}
