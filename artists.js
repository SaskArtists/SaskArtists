/*
	How To Add Data
	
	Get lat and long of a location: http://itouchmap.com/latlong.html
	
	
*/

var macDoList = [
  //{lat:49.633567,lng:-105.991792,data:{name:"Assiniboia"}},

  {lat:50.946830,lng:-104.211685,data:{name:"Cupar"}},
  
  {lat:53.566667,lng:-105.883333,data:{name:"Emma Lake"}},
  //{lat:49.139084,lng:-102.991481,data:{name:"Estevan"}},

  {lat:50.768051,lng:-103.782955,data:{name:"Fort Qu' Appelle"}},

  {lat:51.059435,lng:-103.182622,data:{name:"Goodeve"}},

  {lat:52.201979,lng:-105.122865,data:{name:"Humboldt"}},

  {lat:50.048963,lng:-102.302054,data:{name:"Langbank"}},
  {lat:52.358978,lng:-106.958358,data:{name:"Langham"}},
  {lat:50.646281,lng:-104.867569,data:{name:"Lumsden"}},

  {lat:52.100418,lng:-105.761042,data:{name:"Meacham"}},
  {lat:50.391142,lng:-105.535049,data:{name:"Moose Jaw"}},

  {lat:53.362353,lng:-104.013005,data:{name:"Nipawin"}},
  {lat:52.772884,lng:-108.299656,data:{name:"North Battleford"}},

  {lat:53.199267,lng:-105.754261,data:{name:"Prince Albert"}},

  {lat:49.460820,lng:-104.297090,data:{name:"Radville"}},
  {lat:52.449594,lng:-108.258470,data:{name:"Red Pheasant Reserve"}},
  {lat:50.449766,lng:-104.614944,data:{name:"Regina"}},  {lat:50.188243,lng:-104.907799,data:{name:"Rouleau"}},

  {lat:50.432234,lng:-101.546351,data:{name:"Sainte-Marthe"}},
  {lat:52.125606,lng:-106.670074,data:{name:"Saskatoon"}},
  {lat:50.285069,lng:-107.797172,data:{name:"Swift Current"}},

  {lat:52.443732,lng:-109.158319,data:{name:"Unity"}},

  //{lat:49.663284,lng:-103.853291,data:{name:"Weyburn"}},

  //{lat:51.213889,lng:-102.462778,data:{name:"Yorkton"}},

];

var artists = [
//A
//B
	{name:"Lorne Beug",link:'lbeug/index.html',city:'Regina'},
	{name:"Ronald Bloore",link:'rbloore/index.html',city:'Regina'},
	{name:"Mel Bolen",link:'mbolen/index.html',city:'Humboldt'},
	{name:"Robert Boyer",link:'rboyer/index.html',city:'Prince Albert'},
//C
	{name:"David Clausen",link:'clausen/index.html',city:'Regina'},
	{name:"Alex Crease",link:'acrease/index.html',city:'Regina'},
//D
	{name:"Joyce Deutscher",link:'jdeutscher/index.html',city:'Regina'},
//E
	{name:"Emma Lake Artists' Workshops",link:'emmalake/index.html',city:'Emma Lake'},	
	{name:"Carole Epp",link:'cepp/index.html',city:'Saskatoon'},
//F
	{name:"Joe Fafard",link:'jfafard/index.html',city:'Sainte-Marthe'},
	{name:"Charley Farrero",link:'cfarrero/index.html',city:'Meacham'},
	{name:"Amber Fyfe",link:'afyfe/index.html',city:'Regina'},
//G	
	{name:"Grace Garden",link:'ggarden/index.htm',city:'Regina'},
	{name:"David Garneau",link:'dgarneau/index.html',city:'Regina'},
	{name:"David Gilhooly",link:'dgilhooly/index.html',city:'Regina'},
	{name:"Brian Gladwell",link:'bgladwell/index.html',city:'North Battleford'},
	{name:"Jesse Goddard",link:'jgoddard/index.html',city:'Regina'},
	{name:"Ted Godwin",link:'tgodwin/index.html',city:'Regina'},
//H
	{name:"Folmer Hansen",link:'fhansen/index.html',city:"Fort Qu' Appelle"},
	{name:"Iris Hauser",link:'ihauser/index.html',city:'Saskatoon'},
	{name:"Joel Hustak",link:'jhustak/index.html',city:'Regina'},
//I
	{name:"Roger Ing",link:'ring/index.htm',city:'Regina'},
//J
	{name:"June Jacobs",link:'jjacobs/index.html',city:'Meacham'},
//K
	{name:"Augustus Kenderdine",link:'akenderdine/index.html',city:'Saskatoon'},
	{name:"Andrew King",link:'aking/index.html',city:'Regina'},
	{name:"Dorothy Knowles",link:'dknowles/dknolews.html',city:'Unity'},
	//{name:"William Kurelek",link:'wkurelek/dknolews.html',city:'??'},
//L
	{name:"Marilyn Levine",link:'mlevine/index.htm',city:'Regina'},
	{name:"Earnest Lindner",link:'elindner/index.html',city:'Saskatoon'},
	{name:"Anthony Linklater",link:'anthony/index.htm',city:'Regina'},
	{name:"Kenneth Lochhead",link:'klochhead/home.html',city:'Regina'},
	{name:"David Loran",link:'dloran/index.html',city:'Regina'},
//M
	{name:"Terence John Marner",link:'tmarner/index.html',city:'Regina'},
	{name:"Pete Makarow",link:'pmakarow/index.html',city:'Regina'},
	{name:"Ahasiw Maskegon-Iskew",link:'ahasiw/index.htm',city:'Regina'},
	{name:"Art McKay",link:'amckay/info.html',city:'Nipawin'},
	{name:"Scott McLeod",link:'smcleod/index.htm',city:'Radville'},
	{name:"June Mitchell",link:'jmitchell/index.html',city:'Regina'},
	{name:"Joni Mitchell",link:'jmitchell2/index.html',city:'North Battleford'},
	{name:"Douglas Morton",link:'dmorton/index.html',city:'Regina'},
	{name:"Gerald Morton",link:'gmorton/index.html',city:'Langbank'},
//N
	{name:"John Nugent",link:'jnugent/index.html',city:'Lumsden'},
//O
	{name:"Jean Oser",link:'joser/index.html',city:'Regina'},
//P
	{name:"Wendy Parsons",link:'wparsons/index.html',city:'Moose Jaw'},
	{name:"Maija Peeples-Bright",link:'mpeeples/index.html',city:'Regina'},
	{name:"William Perehudoff",link:'wperehudoff/index.html',city:'Langham'},
	{name:"Edward Poitras",link:'epoitras/index.html',city:'Regina'},
//R
	{name:"Regina 5",link:'regina_5/index.html',city:'Regina'},
	{name:"Susan Rankin",link:'srankin/index.html',city:'Moose Jaw'},
	{name:"Anita Rocamora",link:'arocamora/index.html',city:'Meacham'},
//S
	{name:"Gerald Saul",link:'gsaul/index2.html',city:'Regina'},
	{name:"Gerri Ann Siwek",link:'gsiwek/index.html',city:'Regina'},
	{name:"Allen Sapp",link:'asapp/index.html',city:'Red Pheasant Reserve'},
	{name:"Jack Severson",link:'jseverson/index.htm',city:'Regina'},
	{name:"Mark Sexton",link:'msexton/index.html',city:'Regina'},
	{name:"Christine Shaw",link:'cshaw/index.html',city:'Regina'},
	{name:"Inglis Sheldon-Williams",link:'inglis/index.html',city:'Regina'},
	{name:"Dmytro Stryjek",link:'dstryjek/index.html',city:'Saskatoon'},
	{name:"Jack Sures",link:'jsures/index.html',city:'Regina'},
//T	
	{name:"F. Wayne Tunison",link:'wtunison/index.htm',city:'Regina'},
	{name:"Marlo V",link:'mv/index.html',city:'Cupar'},
//U
//V
	{name:"Jon Vickers",link:'jvickers/index.html',city:'Prince Albert'},
//W
	{name:"Zane Wilcox",link:'zwilcox/index.html',city:'Saskatoon'},
	{name:"Sean Whalley",link:'swhalley/index.html',city:'Regina'},
//Y
	{name:"Dyson Yobb",link:'dyobb/index.html',city:'Regina'},
	{name:"Russell Yuristy",link:'ryuristy/index.html',city:'Goodeve'},
//Z
	{name:"Andrew King",link:'aking/index.html',city:'Rouleau'},
];