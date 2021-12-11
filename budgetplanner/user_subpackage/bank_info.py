class password:
    def __init__(self,userid,password):
        self.userid = userid
        self.password = password
        class Error(Exception):
            pass
        class PasswordTooSmallError(Error):
            pass
        class PasswordTooLargeError(Error):
            pass
        try:
            if len(self.password) < 7:
                raise PasswordTooSmallError
            elif len(self.password) > 15:
                raise PasswordTooLargeError
        except PasswordTooSmallError:
            print("Password lenth is too small.")
        except PasswordTooLargeError:
            print("Password lenth is too large.")
        
    def update(self,newuserid, newpassword):
        self.userid = newuserid
        self.password = newpassword
        return self.userid,self.password

    def show(self):
        print('userid: {} password: {}'.format(self.userid,self.password))

    def delete(self):
        self.userid = ''
        self.password = ''
        return self.userid,self.password
 