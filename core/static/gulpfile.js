'use strict';

var gulp = require('gulp');
var	sass = require('gulp-sass'); //var	sass = require('gulp-ruby-sass');
var watch = require('gulp-watch');
	

// task para o sass
gulp.task('sass', function () {
	return gulp.src('sass/**/*.sass') 
	.pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError)) 
	.pipe(gulp.dest('css')); 
});

//task para o watch
gulp.task('watch', function () { 
	gulp.watch('sass/**/*.sass', gulp.series('sass')); 
});

//task default gulp
gulp.task('default', gulp.series('sass', 'watch'));