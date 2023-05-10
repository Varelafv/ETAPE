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
signal  Data : std_logic_vector(12 downto 0);
signal Gating1 : std_logic_vector(2 downto 0);
signal Gating2: std_logic_vector(2 downto 0);
signal Slt_freq1 : std_logic_vector(3 downto 0);
signal Slt_freq2 : std_logic_vector(3 downto 0);

component CEMES_IP_SPLIT_MIO
    Port (clk : in std_logic;
          DATA_IN : in std_logic_vector (12 downto 0):=(others=>'0');
          Type_Wave_OUT1 : out std_logic_vector (2 downto 0):=(others=>'0');
          Type_Wave_OUT2 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_CH1 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_CH2 : out std_logic_vector (2 downto 0):=(others=>'0');
          Select_frequence_CH1 : out std_logic_vector(3 downto 0):=(others=>'0');
          Select_frequence_CH2 : out std_logic_vector(3 downto 0):=(others=>'0')
          );

 end component ;

begin

UP:  CEMES_IP_SPLIT_MIO port map(clk =>clk ,DATA_IN=>Data,Type_Wave_OUT1=>Type1,Type_Wave_OUT2=> Type2,GATING_CH1=>Gating1,GATING_CH2=>Gating2, Select_frequence_CH1=>Slt_freq1,Select_frequence_CH2=>Slt_freq2);

genere: process
begin
       Data<="0000000100100";
       clk<='1';
       wait for 60 ns;
       Data<="0000000100101";
       clk<='0';
       wait for 60 ns;
       Data<="0000000100110";
       clk<='1';
       wait for 60 ns;
       Data<="0000000100100";
       clk<='0';
       wait for 60 ns;
end process; 
end Behavioral;
