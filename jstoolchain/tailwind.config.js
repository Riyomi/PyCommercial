module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      screens: {
        phone: "480px" /* mid-size phones */,
        tablet:
          "600px" /* portrait tablets, portrait iPad, e-readers (Nook/Kindle) */,
        landscapetablet:
          "801px" /* tablet, landscape iPad, lo-res laptops ands desktops */,
        laptop: "1025px" /* big landscape tablets, laptops, and desktops */,
        desktop: "1281px" /* hi-res laptops and desktops */,
      },
    },
  },
  variants: {
    opacity: ({ after }) => after(["disabled"]),
  },
  plugins: [],
};
