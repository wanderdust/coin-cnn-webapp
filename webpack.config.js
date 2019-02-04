const path = require('path');
const webpack = require('webpack');
const dotenv = require('dotenv');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

process.env.NODE_ENV = process.env.NODE_ENV || 'development';

if (process.env.NODE_ENV === 'test') {
  dotenv.config({ path: '.env.test' });
} else if (process.env.NODE_ENV === 'development') {
  dotenv.config({ path: '.env.development' });
}

// We wrap all in a function to get access to the env variable.
module.exports = (env) => {
  const isProduction = env === 'production';
  // Name of the file where css files are going to get extracted to.
  const CSSExtract = new MiniCssExtractPlugin({ filename: 'styles.css' });

  return {
    mode: 'none',
    /*
    * Babel-polyfill: adds support of ES6/7 features for older browsers.
    * app.js is the entry file that gets compiled.
    */
    entry: ['babel-polyfill', './src/app.js'],
    // The final file where compiled data is sent to (bundle.js).
    output: {
      path: path.join(__dirname, 'static', 'dist'),
      filename: 'bundle.js'
    },
    module: {
      // What webpack needs to do when parsing the data to the output file (bundle.js).
      rules: [{
        /*
        * babel-loader: convert all ES6 to ES5.
        * babel configuration is done over in the '.babelrc' file.
        */
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/
      },
      {
        test: /\.svg$/,
        loader: 'svg-inline-loader'
      },
      {
        /*
        * Convert scss into normal css and pass it as styles to javascript.
        * sourceMap: true shows where the css lives in the pre-compiled files.
        */
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              sourceMap: true
            }
          }, {
            loader: 'sass-loader',
            options: {
              sourceMap: true
            }
          }
        ],
        test: /\.s?css$/
      }]
    },
    plugins: [
      CSSExtract,
      new webpack.DefinePlugin({
        'process.env.FIREBASE_API_KEY': JSON.stringify(process.env.FIREBASE_API_KEY),
        'process.env.FIREBASE_AUTH_DOMAIN': JSON.stringify(process.env.FIREBASE_AUTH_DOMAIN),
        'process.env.FIREBASE_DATABASE_URL': JSON.stringify(process.env.FIREBASE_DATABASE_URL),
        'process.env.FIREBASE_PROJECT_ID': JSON.stringify(process.env.FIREBASE_PROJECT_ID),
        'process.env.FIREBASE_STORAGE_BUCKET': JSON.stringify(process.env.FIREBASE_STORAGE_BUCKET),
        'process.env.FIREBASE_MESSAGING_SENDER_ID': JSON.stringify(process.env.FIREBASE_MESSAGING_SENDER_ID)
      })
    ],
    /*
    * Hashmap for debugging. Shows error in pre-compiled files rather than in bundle.js.
    * If !isProduction we use a faster compiler for dev - inline-source-map.
    * source map is really slow for dev but really fast for production.
    */
    devtool: isProduction ? 'source-map' : 'inline-source-map',
    // Webpack server for development.
    devServer: {
      contentBase: path.join(__dirname, 'static'),
      // We tell the server we will be using React for routing and not the server.
      historyApiFallback: true,
      publicPath: '/dist/',
      proxy: {
        '/api': 'http://localhost:5000'
      }
    }
  };
};
