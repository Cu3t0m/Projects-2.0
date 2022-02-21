module Main where

import Lib
-- import Text.Read (Lexeme(String))
import Control.Monad.ST ( runST )
import Control.Monad ( forM_ )
import Data.STRef ( modifySTRef, newSTRef, readSTRef )

sumST :: Num a => [a] -> a
sumST xs = runST $ do

    n <- newSTRef 0

    forM_ xs $ \x -> do
        modifySTRef n (+x)

    readSTRef n


x :: Integer
x = 0

doubleUp :: Integer -> Integer
doubleUp a = a * 2

uwu :: String
uwu = "uwu"

main :: IO ()
main = do
    print uwu
    print x
    print y