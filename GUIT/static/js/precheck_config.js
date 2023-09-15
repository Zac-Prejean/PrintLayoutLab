
// DESKPLATES
const prefixDSWCLR001 = "DSWCLR001";  
const deskplates = [

"UVPCCACRP3UVP", "UVPPSTNPWUVP", "UVPPSJOSHDNPUVP","UVPUYACPFUVP", "UVPUYACSFUVP", "UVPUYTEAPLUVP",
"UVPUYACSTUVP", 

"UVPCCACRPWHUVP", "UVPCCACRP2UVP", "UVPCCACRPGLCUVP", "UVPCCACRPSCUVP", 

"UVPJMZZCLASSDNUVP","UVPPSCFDNPUVP", "UVPJMZZFLOWDNPUVP", "UVPPSFLOWDNPUVP","UVPJMZZDNP2UVP", 
"UVPPSZZDNPBUVP", "UVPPSLAWDNPUVP","UVPPSTDSJHUVP", "UVPPSTDSASUVP", 

"UVPPSZACH2UVP", "UVPPSZACH68UVP", "UVPPSZACH6969UVP", 
"UVPPSZACH69UVP"];

const validSkus_deskplates = deskplates.map(suffix => prefixDSWCLR001 + suffix);

// 16oz TUM COLORS 
const prefixACSKTUM16ZPNK = "ACSKTUM16ZPNK";
const prefixACSKTUM16ZBLK = "ACSKTUM16ZBLK";
const prefixACSKTUM16ZICB = "ACSKTUM16ZICB";
const prefixACSKTUM16ZMNT = "ACSKTUM16ZMNT";

// 18oz TUM COLORS 
const prefixACSKTUM18ZDBL = "ACSKTUM18ZDBL";
const prefixACSKTUM18ZCLGD = "ACSKTUM18ZCLGD";
const prefixACSKTUM18ZCLRGD = "ACSKTUM18ZCLRGD";
  
const oneLineTum = [

    "UVPUYPTBFUVP", "UVPPSACRYLMIUVP", "UVPPSSCCPTUVP", "UVPPSPICBFUVP", "uvpuysdd2uvp", "UVPRADENTUVP", 

    "UVPANWHTUVP", "UVPPSTBUVP", "UVPPSKFGPUVP", "UVPPSKFGWUVP",
    
    "UVPPSDENTTELUVP", "UVPPSDENTBLKUVP", "UVPPSDENTPNKUVP",
    
    "UVPPSKIDTBUVP", "UVPPSKIDTWUVP", "UVPPSKIDTPUVP",
    
    "UVPUYSTD1UVP","uvpuystd2uvp", "UVPUYSTD3UVP", "UVPUYSTD4UVP", "UVPUYSTD5UVP", "UVPUYSTD6UVP", "UVPUYSTD7UVP",
    
    "UVPPSAPPTUVP", "UVPPSABCTUVP", "UVPPSPENTUVP", "UVPPSBUSTUVP",
    
    "UVPJMKTDSUVP", "UVPJMKTMTUVP", "UVPJMKTPCUVP", "UVPJMKTUCUVP",
    
    "UVPPSB16BUVP", "UVPPSB16WUVP", "UVPPSTTUMBUVP", "UVPPSTTUMWUVP", "UVPPSPHRMBUVP", "UVPPSPHRMWUVP", "UVPPSSTILGBHUVP",
    "UVPPSSTILGWHUVP", "UVPJMSLCLBUVP", "UVPJMSLCLWUVP", "UVPPSNUBRBUVP", "UVPPSNUBRWUVP", "UVPJMHDBSUVP", "UVPJMHDWSUVP",
    "UVPJMHDBPUVP", "UVPJMHDWPUVP",
    
    "UVPPSEITTTSBUVP", "UVPPSEITTTSWUVP", "UVPPSTTPTBUVP", "UVPPSTTPTWUVP", "UVPPSTTPTABUVP", "UVPPSTTPTAWUVP", "UVPPSTTOTBUVP", 
    "UVPPSTTOTWUVP", "UVPPSTTOTABUVP", "UVPPSTTOTAWUVP", "UVPPSSLPTBUVP", "UVPPSSLPTWUVP", "UVPPSOPTTBUVP", "UVPPSOPTTWUVP",

    'UVPPSHSTGUVP', 'UVPPSHSTWUVP', 'UVPPSHSTPUVP', 'UVPPSHSTHUVP',
     ];

const twoLineTum = [ 

    "UVPPSGKNTPUVP", "UVPPSGKNTSUVP", "UVPANWTTUVP",

    "UVPPSVETTBUVP", "UVPPSVETTWUVP", "UVPCCGTUMBUVP", "UVPCCGTUMWUVP", "UVPJMMAMATBUVP", "UVPJMMAMATWUVP", "UVPPSAUNTTBUVP", 
    "UVPPSAUNTTWUVP"
];
     
  
const validSkus_pinkTum = oneLineTum.map(suffix => prefixACSKTUM16ZPNK + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM16ZPNK + suffix));  
const validSkus_blackTum = oneLineTum.map(suffix => prefixACSKTUM16ZBLK + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM16ZBLK + suffix));  
const validSkus_iceTum = oneLineTum.map(suffix => prefixACSKTUM16ZICB + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM16ZICB + suffix));  
const validSkus_mintTum = oneLineTum.map(suffix => prefixACSKTUM16ZMNT + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM16ZMNT + suffix));  
  
const validSkus_dustyblueTum = oneLineTum.map(suffix => prefixACSKTUM18ZDBL + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM18ZDBL + suffix));  
const validSkus_goldTum = oneLineTum.map(suffix => prefixACSKTUM18ZCLGD + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM18ZCLGD + suffix));  
const validSkus_rosegoldTum = oneLineTum.map(suffix => prefixACSKTUM18ZCLRGD + suffix).concat(twoLineTum.map(suffix => prefixACSKTUM18ZCLRGD + suffix)); 

// NECKLACES
const prefixNCK = "NCK";
const oneLineNck = [

"GLDCHN01", "SILCHN01", "RSGCHN01",];

const twoLineNck = [

"02GLDCHN01", "02SILCHN01", "02RSGCHN01"];

const threeLineNck = [

"03GLDCHN01", "03SILCHN01", "03RSGCHN01"];

const fourLineNck = [

"04GLDCHN01", "04SILCHN01", "04RSGCHN01"];

const validSkus_1neckless = oneLineNck.map(suffix => prefixNCK + suffix);
const validSkus_2neckless = twoLineNck.map(suffix => prefixNCK + suffix);
const validSkus_3neckless = threeLineNck.map(suffix => prefixNCK + suffix);
const validSkus_4neckless = fourLineNck.map(suffix => prefixNCK + suffix);

// RINGS
const prefixRNG = "RNG";
const oneLineRNG = [

];

const twoLineRNG = [

"35GLD", "35SIL", "35RSG", "46GLD", "46SIL", "46RSG", "68GLD", "68SIL", "68RSG", "78GLD", "78SIL", "78RSG",
"910GLD", "911SIL", "910RSG", "911GLD", "911SIL", "911RSG", 
"DBL35GLD", "DBL35SIL", "DBL35RSG", "DBL46GLD", "DBL46SIL", "DBL46RSG", "DBL68GLD", "DBL68SIL", "DBL68RSG", 
"DBL78GLD", "DBL78SIL", "DBL78RSG", "DBL910GLD", "DBL910SIL", "DBL910RSG", "DBL911GLD", "DBL911SIL", "DBL911RSG",
];


const validSkus_1ring = oneLineRNG.map(suffix => prefixRNG + suffix);
const validSkus_2ring = twoLineRNG.map(suffix => prefixRNG + suffix);



export { prefixACSKTUM16ZPNK, prefixACSKTUM16ZBLK, prefixACSKTUM16ZICB, prefixACSKTUM16ZMNT, prefixACSKTUM18ZDBL, prefixACSKTUM18ZCLGD, 
    prefixACSKTUM18ZCLRGD, prefixNCK, prefixRNG, oneLineTum, oneLineNck, twoLineNck, threeLineNck, fourLineNck, oneLineRNG, twoLineRNG};  
    
export const validSkus = [...validSkus_deskplates, ...validSkus_pinkTum, ...validSkus_blackTum, ...validSkus_iceTum, ...validSkus_mintTum, 
    ...validSkus_dustyblueTum, ...validSkus_goldTum, ...validSkus_rosegoldTum, ...validSkus_dustyblueTum, ...validSkus_1neckless, 
    ...validSkus_2neckless, ...validSkus_3neckless, ...validSkus_4neckless, ...validSkus_1ring, ...validSkus_2ring];