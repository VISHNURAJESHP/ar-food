import { Flex,Button} from "@chakra-ui/react"
import { Search } from "./Search"
import { CartIcon } from "../dashboard/index";
import  {useRouter} from "next/navigation"

export const TopBar = () => {
  const router = useRouter()
  return (
    <Flex minH="20vh" justifyContent="space-between" alignItems="center" px="30px">
        <Button onClick={()=>router.push("/login")}>Login</Button>
        <Search />
        <CartIcon />
      </Flex>
  )
}