// eslint-disable-next-line @typescript-eslint/no-var-requires
const BundleTracker = require("webpack-bundle-tracker")

let config = {
  assetsDir: "static/vue"
}

if (process.env.NODE_ENV === "production") {
  config = Object.assign(config, {
    configureWebpack: {
      plugins: [new BundleTracker({ filename: "dist/webpack-stats.json" })]
    }
  })
}

module.exports = config
