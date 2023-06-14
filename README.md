# ETAPE
----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 13.06.2023 15:14:55
-- Design Name: 
-- Module Name: MAP_WGEN - Behavioral
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

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity MAP_WGEN is
    Port (clk : in std_logic;
          DATA_IN : in STD_LOGIC_VECTOR (15 downto 0);
          ADR_IN : in STD_LOGIC_VECTOR (7 downto 0);
          CMD_IN : in STD_LOGIC_VECTOR (3 downto 0);
          TYPE_WAVE_1 : out std_logic_vector (2 downto 0):=(others=>'0');
          TYPE_WAVE_2 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_1 : out std_logic_vector (2 downto 0):=(others=>'0');
          GATING_2 : out std_logic_vector (2 downto 0):=(others=>'0');
          SEL_FREQ_1 : out std_logic_vector(3 downto 0):=(others=>'0');
          SEL_FREQ_2 : out std_logic_vector(3 downto 0):=(others=>'0')
          );
   
end MAP_WGEN;

architecture Behavioral of MAP_WGEN is
--    signal ADRESS : std_logic_vector (1 downto 0) := (others => '0'); --[0 1 2 3 ]
--    signal W : std_logic := '0';
--    signal R : std_logic := '0';
--    signal CHANNEL1, CHANNEL2 : std_logic := '0';
--    signal DATA : std_logic_vector (7 downto 0) := (others => '0');
--	signal signal_Type_Wave_OUT1,signal_Type_Wave_OUT2 : std_logic_vector (2 downto 0) := (others => '0'); 

signal reset_MIO, rd_MIO, wr_MIO : std_logic;
signal wren_typ_wav_1, wren_typ_wav_2 : std_logic;
signal wren_GATING_1 , wren_GATING_2 :  std_logic;
signal wren_SEL_FREQ_1, wren_SEL_FREQ_2 :  std_logic;


begin

reset_MIO <= CMD_IN(0);      --reset soft
rd_MIO <= CMD_IN(1);
wr_MIO <= CMD_IN(2);

--channel1
wren_typ_wav_1 <= '1' when ADR_IN=x"00" AND wr_MIO='1' else '0' ;
wren_GATING_1 <= '1' when ADR_IN=x"01" AND wr_MIO='1' else '0' ; 
wren_SEL_FREQ_1<= '1' when ADR_IN=x"02" AND wr_MIO='1' else '0' ; 
--channel2
wren_typ_wav_2 <= '1' when ADR_IN=x"03" AND wr_MIO='1' else '0' ;
wren_GATING_2 <= '1' when ADR_IN=x"04" AND wr_MIO='1' else '0' ;
wren_SEL_FREQ_2<= '1' when ADR_IN=x"05" AND wr_MIO='1' else '0' ; 
-------------------------channel1-----------------------
process (clk, reset_MIO, wren_typ_wav_1)
	begin
	if reset_MIO ='1' then
	   TYPE_WAVE_1 <="111" ;
	elsif rising_edge(clk) and wren_typ_wav_1='1' then
	   TYPE_WAVE_1 <= DATA_IN(2 downto 0) ;
	end if;
	end process;
	
process (clk, reset_MIO, wren_GATING_1)
	begin
	if reset_MIO ='1' then
	   GATING_1 <="111" ;
	elsif rising_edge(clk) and wren_GATING_1='1' then
	   GATING_1 <= DATA_IN(2 downto 0) ;
	end if;
	end process;
	
process (clk, reset_MIO, wren_SEL_FREQ_1)
	begin
	if reset_MIO ='1' then
	   SEL_FREQ_1 <="1111" ;
	elsif rising_edge(clk) and wren_SEL_FREQ_1='1' then
	   SEL_FREQ_1 <= DATA_IN(3 downto 0) ;
	end if;
	end process;
	
-------------------------channel2-----------------------	
process (clk, reset_MIO, wren_typ_wav_2)
	begin
	if reset_MIO ='1' then
	   TYPE_WAVE_2 <="111" ;
	elsif rising_edge(clk) and wren_typ_wav_1='1' then
	   TYPE_WAVE_2 <= DATA_IN(2 downto 0) ;
	end if;
	end process;
	
process (clk, reset_MIO, wren_GATING_2)
	begin
	if reset_MIO ='1' then
	   GATING_2 <="111" ;
	elsif rising_edge(clk) and wren_GATING_2='1' then
	   GATING_2 <= DATA_IN(2 downto 0) ;
	end if;
	end process;
	
process (clk, reset_MIO, wren_SEL_FREQ_2)
	begin
	if reset_MIO ='1' then
	   SEL_FREQ_2 <="1111" ;
	elsif rising_edge(clk) and wren_SEL_FREQ_2='1' then
	   SEL_FREQ_2 <= DATA_IN(3 downto 0) ;
	end if;
	end process;



end Behavioral;
