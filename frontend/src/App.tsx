import { useState } from 'react';
import Select from 'react-select';
import styled from 'styled-components';
import './App.css';

interface OptionType {
  value: string;
  label: string;
}

const Button = styled.button`
  background: transparent;
  color: white;
  font-size: 20px;
  padding: 10px 60px;
  border-radius: 5px;
  border: 2px solid white;
  margin: 10px 0px;
  cursor: pointer;
  const Button = styled.button
`;

function App(this: any) {

  const options: OptionType[] = [
    { value: "Nishi-magome", label: "Nishi-magome" },
    { value: "Magome", label: "Magome" },
    { value: "Nakanobu", label: "Nakanobu" },
    { value: "Togoshi", label: "Togoshi" },
    { value: "Gotando", label: "Gotando" },
    { value: "Takanawadai", label: "Takanawadai" },
    { value: "Sengakuji", label: "Sengakuji" },
    { value: "Mita", label: "Mita" },
    { value: "Daimon", label: "Daimon" },
    { value: "Shimbashi", label: "Shimbashi" },
    { value: "Higashi-ginza", label: "Higashi-ginza" },
    { value: "Takaracho", label: "Takaracho" },
    { value: "Nihombashi", label: "Nihombashi" },
    { value: "Ningyocho", label: "Ningyocho" },
    { value: "Higashi-Nihombashi", label: "Higashi-Nihombashi" },
    { value: "Asakusabashi", label: "Asakusabashi" },
    { value: "Kuramae", label: "Kuramae" },
    { value: "Asakusa", label: "Asakusa" },
    { value: "Honjo-azumabashi", label: "Honjo-azumabashi" },
    { value: "Oshiage <SKYTREE>", label: "Oshiage <SKYTREE>" },
    { value: "Yoyogi-uehara", label: "Yoyogi-uehara" },
    { value: "Yoyogi-koen", label: "Yoyogi-koen" },
    { value: "Meiji-jingumae <Harajuku>", label: "Meiji-jingumae <Harajuku>" },
    { value: "Omote-sando", label: "Omote-sando" },
    { value: "Nogizaka", label: "Nogizaka" },
    { value: "Akasaka", label: "Akasaka" },
    { value: "Kokkai-gijidomae", label: "Kokkai-gijidomae" },
    { value: "Kasumigaseki", label: "Kasumigaseki" },
    { value: "Hibiya", label: "Hibiya" },
    { value: "Nijubashimae <Marunouchi>", label: "Nijubashimae <Marunouchi>" },
    { value: "Otemachi", label: "Otemachi" },
    { value: "Shin-ochanomizu", label: "Shin-ochanomizu" },
    { value: "Yushima", label: "Yushima" },
    { value: "Nezu", label: "Nezu" },
    { value: "Sendagi", label: "Sendagi" },
    { value: "Nishi-nippori", label: "Nishi-nippori" },
    { value: "Machiya", label: "Machiya" },
    { value: "Kita-senju", label: "Kita-senju" },
    { value: "Ayase", label: "Ayase" },
    { value: "Kita-ayase", label: "Kita-ayase" },
    { value: "Shinjuku-nishiguchi", label: "Shinjuku-nishiguchi" },
    { value: "Hagashi-shinjuku", label: "Hagashi-shinjuku" },
    { value: "Wakamatsu-kawada", label: "Wakamatsu-kawada" },
    { value: "Ushigome-Yanagicho", label: "Ushigome-Yanagicho" },
    { value: "Ushigome-kagurazaka", label: "Ushigome-kagurazaka" },
    { value: "Lidabashi", label: "Lidabashi" },
    { value: "Kasuga", label: "Kasuga" },
    { value: "Hongo-sanchome", label: "Hongo-sanchome" },
    { value: "Ueno-okachimachi", label: "Ueno-okachimachi" },
    { value: "Shin-okachimachi", label: "Shin-okachimachi" },
    { value: "Ryogoku", label: "Ryogoku" },
    { value: "Morishita", label: "Morishita" },
    { value: "Kiyosumi", label: "Kiyosumi" },
    { value: "Monzen-nakacho", label: "Monzen-nakacho" },
    { value: "Tsukishima", label: "Tsukishima" },
    { value: "Kachidoki", label: "Kachidoki" },
    { value: "Tsukijishijo", label: "Tsukijishijo" },
    { value: "Shiodome", label: "Shiodome" },
    { value: "Akabanebashi", label: "Akabanebashi" },
    { value: "Azabu-juban", label: "Azabu-juban" },
    { value: "Roppongi", label: "Roppongi" },
    { value: "Aoyama-itchome", label: "Aoyama-itchome" },
    { value: "Kokuritsu-kyogijo", label: "Kokuritsu-kyogijo" },
    { value: "Yoyogi", label: "Yoyogi" },
    { value: "Shinjuku", label: "Shinjuku" },
    { value: "Tochomae", label: "Tochomae" },
    { value: "Nishi-shinjuku-gochome", label: "Nishi-shinjuku-gochome" },
    { value: "Nakano-sakaue", label: "Nakano-sakaue" },
    { value: "Higashi-nakano", label: "Higashi-nakano" },
    { value: "Nakai", label: "Nakai" },
    { value: "Ochiai-minami-nagasaki", label: "Ochiai-minami-nagasaki" },
    { value: "Shin-egato", label: "Shin-egato" },
    { value: "Netima", label: "Netima" },
    { value: "Toshimaen", label: "Toshimaen" },
    { value: "Naerima-kasugacho", label: "Naerima-kasugacho" },
    { value: "Hikarigaoka", label: "Hikarigaoka" },
    { value: "Wakoshi", label: "Wakoshi" },
    { value: "Chikatetsu-narimasu", label: "Chikatetsu-narimasu" },
    { value: "Chikatetsu-akatsuka", label: "Chikatetsu-akatsuka" },
    { value: "Heiwadai", label: "Heiwadai" },
    { value: "Hikawadai", label: "Hikawadai" },
    { value: "Kotake-mukaihara", label: "Kotake-mukaihara" },
    { value: "Senkawa", label: "Senkawa" },
    { value: "Kanamecho", label: "Kanamecho" },
    { value: "Ikebukuro", label: "Ikebukuro" },
    { value: "Zoshigaya", label: "Zoshigaya" },
    { value: "Nishi-waseda", label: "Nishi-waseda" },
    { value: "Higashi-shinjuku", label: "Higashi-shinjuku" },
    { value: "Shinjuku-sanchome", label: "Shinjuku-sanchome" },
    { value: "Kita-sando", label: "Kita-sando" },
    { value: "Shibuya", label: "Shibuya" },
    { value: "Ometo-sando", label: "Ometo-sando" },
    { value: "Gaiemmae", label: "Gaiemmae" },
    { value: "Akasaka-mitsuke", label: "Akasaka-mitsuke" },
    { value: "Tameiki-sanno", label: "Tameiki-sanno" },
    { value: "Toranomon Hills", label: "Toranomon Hills" },
    { value: "Ginza", label: "Ginza" },
    { value: "Kyobashi", label: "Kyobashi" },
    { value: "Mitsukoshimae", label: "Mitsukoshimae" },
    { value: "Kanda", label: "Kanda" },
    { value: "Suehirocho", label: "Suehirocho" },
    { value: "Ueno-hirokoji", label: "Ueno-hirokoji" },
    { value: "Ueno", label: "Ueno" },
    { value: "Inaricho", label: "Inaricho" },
    { value: "Tawaramachi", label: "Tawaramachi" },
    { value: "Naka-meguro", label: "Naka-meguro" },
    { value: "Ebisu", label: "Ebisu" },
    { value: "Hiro-o", label: "Hiro-o" },
    { value: "Kamiyacho", label: "Kamiyacho" },
    { value: "Toranomon-hills", label: "Toranomon-hills" },
    { value: "Tsukiji", label: "Tsukiji" },
    { value: "Hatchobori", label: "Hatchobori" },
    { value: "Kayabacho", label: "Kayabacho" },
    { value: "Kodemmacho", label: "Kodemmacho" },
    { value: "Akihabara", label: "Akihabara" },
    { value: "Naka-okachimachi", label: "Naka-okachimachi" },
    { value: "Iriya", label: "Iriya" },
    { value: "Minowa", label: "Minowa" },
    { value: "Minami-senju", label: "Minami-senju" },
    { value: "Meguro", label: "Meguro" },
    { value: "Shirokanedai", label: "Shirokanedai" },
    { value: "Shirokane-takanawa", label: "Shirokane-takanawa" },
    { value: "Shibakoen", label: "Shibakoen" },
    { value: "Onairimon", label: "Onairimon" },
    { value: "Uchisaiwaicho", label: "Uchisaiwaicho" },
    { value: "Jimbocho", label: "Jimbocho" },
    { value: "Suidobashi", label: "Suidobashi" },
    { value: "Hakusan", label: "Hakusan" },
    { value: "Sengoku", label: "Sengoku" },
    { value: "Sugamo", label: "Sugamo" },
    { value: "Nishi-sugamo", label: "Nishi-sugamo" },
    { value: "Shin-itabashi", label: "Shin-itabashi" },
    { value: "Itabashi-kuyakushomae", label: "Itabashi-kuyakushomae" },
    { value: "Itabashihoncho", label: "Itabashihoncho" },
    { value: "Motohasunuma", label: "Motohasunuma" },
    { value: "Shinmura-sakaue", label: "Shinmura-sakaue" },
    { value: "Shgimura-sanchome", label: "Shgimura-sanchome" },
    { value: "Hasuna", label: "Hasuna" },
    { value: "Nishidai", label: "Nishidai" },
    { value: "Takashimadaira", label: "Takashimadaira" },
    { value: "Shin-takashimadaira", label: "Shin-takashimadaira" },
    { value: "Nishi-takashimadaira", label: "Nishi-takashimadaira" },
    { value: "Ogikubo", label: "Ogikubo" },
    { value: "Minami-asagaya", label: "Minami-asagaya" },
    { value: "Sin-koenji", label: "Sin-koenji" },
    { value: "Higashi-koenji", label: "Higashi-koenji" },
    { value: "Shin-nakano", label: "Shin-nakano" },
    { value: "Nishi-shinjuku", label: "Nishi-shinjuku" },
    { value: "Shinjuku-gyoemmae", label: "Shinjuku-gyoemmae" },
    { value: "Yotsuya-sanchome", label: "Yotsuya-sanchome" },
    { value: "Yotasuya", label: "Yotasuya" },
    { value: "Akasaka-mutsuke", label: "Akasaka-mutsuke" },
    { value: "Kokki-gijidomae", label: "Kokki-gijidomae" },
    { value: "Tokyo", label: "Tokyo" },
    { value: "Awajicho", label: "Awajicho" },
    { value: "Ochanomizu", label: "Ochanomizu" },
    { value: "Korakuen", label: "Korakuen" },
    { value: "Myogadani", label: "Myogadani" },
    { value: "Shin-otsuka", label: "Shin-otsuka" },
    { value: "Nonancho", label: "Nonancho" },
    { value: "Nakano-fujimicho", label: "Nakano-fujimicho" },
    { value: "Nakano-shimbashi", label: "Nakano-shimbashi" },
    { value: "Roppongi-itchome", label: "Roppongi-itchome" },
    { value: "Tameike-sanno", label: "Tameike-sanno" },
    { value: "Nagatacho", label: "Nagatacho" },
    { value: "Yotsuya", label: "Yotsuya" },
    { value: "Ichigaya", label: "Ichigaya" },
    { value: "Iidabashi", label: "Iidabashi" },
    { value: "Todaimae", label: "Todaimae" },
    { value: "Hon-komagome", label: "Hon-komagome" },
    { value: "Komagome", label: "Komagome" },
    { value: "Nishigahara", label: "Nishigahara" },
    { value: "Oji", label: "Oji" },
    { value: "Oji-kamiya", label: "Oji-kamiya" },
    { value: "Shimo", label: "Shimo" },
    { value: "Akabane-iwabuchi", label: "Akabane-iwabuchi" },
    { value: "Akebonobashi", label: "Akebonobashi" },
    { value: "Kudanshita", label: "Kudanshita" },
    { value: "Ogawamachi", label: "Ogawamachi" },
    { value: "Iwamotocho", label: "Iwamotocho" },
    { value: "Bakuro yokoyama", label: "Bakuro yokoyama" },
    { value: "Hamacho", label: "Hamacho" },
    { value: "Kikukawa", label: "Kikukawa" },
    { value: "Sumiyoshi", label: "Sumiyoshi" },
    { value: "Nishi-ojima", label: "Nishi-ojima" },
    { value: "Ojima", label: "Ojima" },
    { value: "Higashi-ojima", label: "Higashi-ojima" },
    { value: "Funabori", label: "Funabori" },
    { value: "Ichinoe", label: "Ichinoe" },
    { value: "Mizue", label: "Mizue" },
    { value: "Shinozaki", label: "Shinozaki" },
    { value: "Motoyawata", label: "Motoyawata" },
    { value: "Nakano", label: "Nakano" },
    { value: "Ochiai", label: "Ochiai" },
    { value: "Takadanobaba", label: "Takadanobaba" },
    { value: "Waseda", label: "Waseda" },
    { value: "Kagurazaka", label: "Kagurazaka" },
    { value: "Takebashi", label: "Takebashi" },
    { value: "Kiba", label: "Kiba" },
    { value: "Toyocho", label: "Toyocho" },
    { value: "Minami-sunamachi", label: "Minami-sunamachi" },
    { value: "Nishi-kasai", label: "Nishi-kasai" },
    { value: "Kasai", label: "Kasai" },
    { value: "Urayasu", label: "Urayasu" },
    { value: "Minami-gyotoku", label: "Minami-gyotoku" },
    { value: "Gyotoku", label: "Gyotoku" },
    { value: "Myoden", label: "Myoden" },
    { value: "Baraki-nakayama", label: "Baraki-nakayama" },
    { value: "Nishi-funabashi", label: "Nishi-funabashi" },
    { value: "Higashi-ikebukuro", label: "Higashi-ikebukuro" },
    { value: "Gokokuji", label: "Gokokuji" },
    { value: "Edogawabashi", label: "Edogawabashi" },
    { value: "Kojimachi", label: "Kojimachi" },
    { value: "Sakuradamon", label: "Sakuradamon" },
    { value: "Yurakucho", label: "Yurakucho" },
    { value: "Ginza-itchome", label: "Ginza-itchome" },
    { value: "Shintomicho", label: "Shintomicho" },
    { value: "Toyosu", label: "Toyosu" },
    { value: "Tatsumi", label: "Tatsumi" },
    { value: "Shin-kiba", label: "Shin-kiba" },
    { value: "Hanzomon", label: "Hanzomon" },
    { value: "Suitengumae", label: "Suitengumae" },
    { value: "Kiyosumi-shirakawa", label: "Kiyosumi-shirakawa" },
    { value: "Kinshicho", label: "Kinshicho" }
  ]

  const [data, setData] = useState({
    distance: 0,
    path_string: "",
    graph: "",
  });

  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [header, setHeader] = useState("Please Input the Start and End Stations");

  // const handleChangeStart = (event: { target: { value: string }; }) => {
  //   setStart(event.target.value);
  // }

  // const handleChangeEnd = (event: { target: { value: string }; }) => {
  //   setEnd(event.target.value);
  // }

  const handleChangeStartSelect = (selectedOption: OptionType | null) => {
    if (selectedOption === null) {
      return;
    }
    setStart(selectedOption['value']);
    console.log(`Option selected:`, selectedOption['value']);
  };
  const handleChangeEndSelect = (selectedOption: OptionType | null) => {
    if (selectedOption === null) {
      return;
    }
    setEnd(selectedOption['value']);
    console.log(`Option selected:`, selectedOption['value']);
  };
  const customStyles = {
    control: (base: any, state: any) => ({
      ...base,
      background: "black",
      borderRadius: state.isFocused ? "3px 3px 0 0" : 3,
      borderColor: state.isFocused ? "white" : "gray",
      "&:hover": {
        borderColor: state.isFocused ? "gray" : "white"
      },
      color: state.selectProps.inputValue ? 'blue' : 'black'
    }),
    input: (base: any) => ({
      ...base,
      color: 'white',
    }),
    option: (provided: any, base: any) => ({
      ...provided,
      backgroundColor: base.isFocused ? "gray" : "black",
    }),
    singleValue: (provided: any) => ({
      ...provided,
      color: 'white',
    }),
    menu: (base: any) => ({
      ...base,
      borderRadius: 2,
      marginTop: 0,
    }),
    menuList: (base: any) => ({
      ...base,
      padding: 0,
      borderRadius: 2,
    })
  };

  const HandleClick = () => {
    setHeader(`Path from ${start} to ${end}`);
    console.log(start, end);
    console.log(`http://localhost:5000/calculate_path/${start}/${end}`);
    fetch(`http://localhost:5000/calculate_path/${start}/${end}`, {
      method: 'GET',
    }).then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        console.log(res);
        return {
          distance: 20,
          path_string: "Monkey",
        }
      }
    })
    .then((data) => {
      console.log(data);
      setData({
        distance: data.distance,
        path_string: data.path_string,
        graph: data.graph || "", // Set data.graph to empty string if data.graph is null or undefined
      });
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
      setData({
        distance: 0,
        path_string: "Incorrect Station Name.",
        graph: "", // Clear the image in case of an error
      });
    });
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>{header}</h1>
        {/* Calling a data from setdata for showing */}
        {/* <input
          type="text"
          value={start}
          onChange={handleChangeStart}
          className="input-field"
        />
        <input
          type="text"
          value={end}
          onChange={handleChangeEnd}
          className="input-field"
        /> */}
        <Select 
          options={options}
          onChange={handleChangeStartSelect}
          placeholder={'Starting Station'}
          className="input-field"
          styles={customStyles}
        />
        <Select 
          options={options}
          onChange={handleChangeEndSelect}
          placeholder={'Destination Station'}
          className="input-field"
          styles={customStyles}
        />

        <Button onClick={HandleClick} className="update-button">
          Find Path
        </Button>
        <div style={{whiteSpace: "pre-wrap"}} id='path-text'>
          <p>{data.path_string}</p>
          <p>Distance: {data.distance.toFixed(2)} km</p>
        </div>
        {data.graph && (
          <img key={data.graph} src={`data:image/png;base64,${data.graph}`} alt="" />
        )}
      </header>
    </div>
  );
}

export default App;
