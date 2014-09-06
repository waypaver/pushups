/*!
 * gulp
 * $ npm install express gulp-ruby-sass gulp-autoprefixer gulp-minify-css gulp-jshint gulp-concat gulp-uglify gulp-imagemin gulp-notify gulp-rename gulp-livereload gulp-cache del --save-dev
 */

// Load plugins
var gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    livereload = require('gulp-livereload'),
    del = require('del');

// Styles
gulp.task('css', function() {
  return gulp.src('assets/styles/scss/main.scss')
    .pipe(sass({ style: 'expanded', }))
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(gulp.dest('static/css/'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(minifycss())
    .pipe(gulp.dest('static/css/'))
    .pipe(notify({ message: 'CSS shit done' }));
});

// Compile copy and minify vendor styles
gulp.task('cssven', function() {
  return gulp.src('assets/styles/css/vendor/*.css', 'assets/styles/scss/vendor/*.scss')
    .pipe(sass({ style: 'expanded', }))
    .pipe(concat('vendor.css'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(minifycss())
    .pipe(gulp.dest('static/css/'))
    .pipe(notify({ message: 'That vendor SCSS & CSS shit is done'}))
})

// Scripts
gulp.task('js', function() {
  return gulp.src('assets/js/*.js')
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter('default'))
    .pipe(concat('main.js'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify())
    .pipe(gulp.dest('static/js/'))
    .pipe(notify({ message: 'JS shit finished' }));
});

// Copy and minify vendor javascript
gulp.task('jsven', function() {
  return gulp.src('assets/js/vendor/**')
    .pipe(concat('vendor.js'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify())
    .pipe(gulp.dest('static/js/'))
    .pipe(notify({ message: 'JS vendor shit copied' }));
})

// Images
gulp.task('img', function() {
  return gulp.src('assets/img/**/*')
    .pipe(cache(imagemin({ optimizationLevel: 3, progressive: true, interlaced: true })))
    .pipe(gulp.dest('static/img/'))
    .pipe(notify({ message: 'Image shit complete' }));
});

// Fonts
gulp.task('copy_fonts', function() {
  gulp.src('assets/fonts/*')
  .pipe(gulp.dest('static/fonts/'));
});

// Clean
gulp.task('clean', function(cb) {
    del(['static/css/', 'static/js/', 'static/img/'], cb)
});

// Default task
gulp.task('default', ['clean'], function() {
    gulp.start('css', 'cssven', 'js', 'jsven', 'img', 'copy_fonts');
});

// Watch
gulp.task('watch', function() {

  // Watch my .scss files
  gulp.watch('assets/styles/scss/*.scss', ['css']);

  //Watch vendor styles
  gulp.watch('assets/styles/css/vendor/*.css', 'assets/styles/scss/vendor/*.scss', ['cssven']);

  // Watch my .js files
  gulp.watch('assets/scripts/**/*.js', ['js']);

  // Watch .js vendor files
  gulp.watch('assets/scripts/vendor/*.js', ['jsven']);

  // Watch image files
  gulp.watch('assets/images/**/*', ['img']);

  //Watch fonts
  gulp.watch('assets/fonts/*.{ttf,woff,eof,svg}', ['copy_fonts']);

  // Create LiveReload server
  livereload.listen();

  // Watch any files in static/, reload on change
  gulp.watch(['static/**']).on('change', livereload.changed);

});