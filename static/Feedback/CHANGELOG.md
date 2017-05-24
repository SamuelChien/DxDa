# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.1.14] - 2016-12-28
### Fixed
- fixed a IE/Edge perf issue due to creation of canvas elements

## [0.1.13] - 2016-12-06
### Added
- language support for pt-BR.

### Fixed
- do not fallback on the global instance of require() if it exists.

## [0.1.12] - 2016-11-29
### Changed
- UI tweaks.

## [0.1.11] - 2016-11-22
### Fixed
- Added return value types to methods in OfficeBrowserFeedback.d.ts.

## [0.1.10] - 2016-11-22
### Added
- A typescript definitions for the package.
- CHANGELOG.md
- LICENSE.md

### Changed
- Passing unknown locale will default to "en" as opposed to throw an exception.
- Uservoice will not be shown for locales other than "en".

### Fixed
- Go to uservoice button was opening a blank page.
