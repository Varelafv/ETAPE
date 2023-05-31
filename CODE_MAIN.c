/******************************************************************************
*
* Copyright (C) 2009 - 2014 Xilinx, Inc.  All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* Use of the Software is limited solely to applications:
* (a) running on a Xilinx device, or
* (b) that interact with a Xilinx device through a bus or interconnect.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* XILINX  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
* OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
*
* Except as contained in this notice, the name of the Xilinx shall not be used
* in advertising or otherwise to promote the sale, use or other dealings in
* this Software without prior written authorization from Xilinx.
*
******************************************************************************/

/*
 * helloworld.c: simple test application
 *
 * This application configures UART 16550 to baud rate 9600.
 * PS7 UART (Zynq) is not initialized by this application, since
 * bootrom/bsp configures it to baud rate 115200
 *
 * ------------------------------------------------
 * | UART TYPE   BAUD RATE                        |
 * ------------------------------------------------
 *   uartns550   9600
 *   uartlite    Configurable only in HW design
 *   ps7_uart    115200 (configured by bootrom/bsp)
 */

#include <stdio.h>
#include "platform.h"
#include "xil_printf.h"
#include "xgpiops.h"
#include "xparameters.h"
#include "xil_printf.h"
#include "init_CT.h"
#include "reception_uart_CT.h"
#include "parse_CT.h"
#include "sleep.h"
static u8 RecvBuffer[TEST_BUFFER_SIZE];
int main()
{
    int valid ; //= 3;
    char dir  ;//= 5;
    char DATA [10];
    int i=0;
    int cpt;

    init_platform();
    init();
    memset(RecvBuffer,0,TEST_BUFFER_SIZE);


    do {
         reception_uart(RecvBuffer);
         xil_printf("%s \n\r",RecvBuffer);
         xil_printf("%c \n\r",RecvBuffer[1]);
         i=0;
        /*for(cpt = 66; cpt>53; cpt--){
            //bus gpio 28bits
            valid = parse_CP(RecvBuffer,&dir,i) ;
            XGpioPs_WritePin(&mio_emio, cpt, dir);
            i++;*/
         XGpioPs_WritePin(&mio_emio, 56, 0x1); //forcer ecriture W=1
         XGpioPs_WritePin(&mio_emio, 57, 0x0); //forcer ecriture R=0
         //CHANNEL CH1-0 CH2-1
         valid = parse_CP(RecvBuffer,&dir,0) ; //RecvBuffer[1]= 0 ou 1 cette valeur sera affecté au channel
         XGpioPs_WritePin(&mio_emio, 58, dir);
         //ADRESS 00 TYPE DE WAVES
         if(RecvBuffer[1]=='W')
			 XGpioPs_WritePin(&mio_emio, 54, 0x0);
			 XGpioPs_WritePin(&mio_emio, 55, 0x0);
         if(RecvBuffer[1]=='G')
        	 XGpioPs_WritePin(&mio_emio, 54, 0x1);
        	 XGpioPs_WritePin(&mio_emio, 55, 0x0);
         if(RecvBuffer[1]=='F')
        	  XGpioPs_WritePin(&mio_emio, 54, 0x0);
        	  XGpioPs_WritePin(&mio_emio, 55, 0x1);

         i=2;


         for(cpt = 66; cpt>58; cpt--){
            //bus gpio 28bits
            valid = parse_CP(RecvBuffer,&dir,i) ;
            XGpioPs_WritePin(&mio_emio, cpt, dir);
            i++;}  //COMMENTER A PARTIR D'ICI

        /*
         usleep(50000);
        //ADRESS TYPE GATING
        XGpioPs_WritePin(&mio_emio, 54, 0x1);
        XGpioPs_WritePin(&mio_emio, 55, 0x0);
        i=9;
        for(cpt = 66; cpt>58; cpt--){
            //bus gpio 28bits
            valid = parse_CP(RecvBuffer,&dir,i) ;
            XGpioPs_WritePin(&mio_emio, cpt, dir);
            i++;}

        usleep(50000);
        //ADRESS TYPE FREQUENCE
        XGpioPs_WritePin(&mio_emio, 54, 0x0);
        XGpioPs_WritePin(&mio_emio, 55, 0x1);
        i=17;
        for(cpt = 66; cpt>58; cpt--){
            //bus gpio 28bits
            valid = parse_CP(RecvBuffer,&dir,i) ;
            XGpioPs_WritePin(&mio_emio, cpt, dir);
            i++;}*/
    }while(1);


    cleanup_platform();
    return 0;
}
