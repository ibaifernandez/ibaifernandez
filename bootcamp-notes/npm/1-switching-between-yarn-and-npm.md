# Switching Between Yarn and NPM

## Things you can’t delete

### packge.json

Do not ever delete this file.

> **This file describes the dependencies that your app requires as well as startup scripts, and is used mutually by both Yarn and NPM. Do not ever delete this file.**

## Things you can delete: folders and files generated during the install process.

### yarn.lock & package-lock.json files

These are the files that are created by NPM and Yarn respectively for their own purposes. These are auto generated and you can delete them at any time, and simply have them be automatically generated again. No worries.

### node_modules folder

This is where the actual packages live after they are installed. However you can install them as many times as you like. So don’t worry about deleting this folder, it is automatically generated and can be regenerated easily.

## Switching Between Package Managers

### From Yarn to NPM

1. Delete the node_modules folder

2. Delete the yarn.lock file

3. Run npm install

    - This will generate a new node_modules folder and a package-lock.json file. Your project is now using NPM.

#### From [ncoughlin](https://ncoughlin.com/posts/switching-yarn-npm/)