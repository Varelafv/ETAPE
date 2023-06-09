----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 02.02.2023 09:57:17
-- Design Name: 
-- Module Name: CEMES_IP_SPLIT_MIO_testbench - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;



entity CEMES_IP_SPLIT_MIO_testbench is
--  Port ( );
end CEMES_IP_SPLIT_MIO_testbench;


architecture Behavioral of CEMES_IP_SPLIT_MIO_testbench is
signal clk : std_logic;
signal Type1,Type2: std_logic_vector(2 downto 0);
signal  Data : std_logic_vector(6 downto 0);
signal Gating : std_logic_vector(2 downto 0);
signal Slt_freq : std_logic_vector(3 downto 0);

component CEMES_IP_SPLIT_MIO
    Port (clk : in std_logic ;
          DATA_IN : in std_logic_vector (6 downto 0):=(others=>'0');
          Type_Wave_OUT1 : out std_logic_vector (2 downto 0):=(others=>'0');
          Type_Wave_OUT2 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING : out std_logic_vector (2 downto 0):=(others=>'0');
          Select_frequence : out std_logic_vector(3 downto 0):=(others=>'0')
          );
 end component ;

begin

UP:  CEMES_IP_SPLIT_MIO port map(clk =>clk ,DATA_IN=>Data,Type_Wave_OUT1=>Type1,
Type_Wave_OUT2=> Type2, GATING=>Gating,Select_frequence =>Slt_freq);

genere: process
begin
       Data<="0101110";
       clk<='1';
       wait for 30 ns;
       Data<="0101110";
       clk<='0';
       wait for 30 ns;
       Data<="0101111";
       clk<='1';
       wait for 30 ns;
       Data<="0101111";
       clk<='0';
       wait for 30 ns;
end process; 
end Behavioral;
